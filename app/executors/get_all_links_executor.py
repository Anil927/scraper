"""A module to extract all the links from the page.

This module contains the GetAllLinksExecutor class that is responsible for extracting all the links from the page.
After extracting the links, it will navigate to each link and extract the data based on the action data provided.
then it will store the data in the database.
"""
import pandas as pd
from playwright.async_api import Playwright

from app.executors.executor_interface import ExecutorInterface
from app.executors.goto_url_executor import GotoUrlExecutor
from app.store.data_collection import DataCollection
from app.store.context_manager import data_store_context_for_every_page
from app.models.action_type import ActionType
import app.actions.action_executor as action_executor
from fastapi_events.dispatcher import dispatch
from app.database_config.database import engine
from app.logger_utils.logger import logger


class GetAllLinksExecutor(ExecutorInterface):
    """class for extracting all the link and then extracting data from each page by navigating to the link."""

    async def execute(self, page: Playwright, action_data: dict[str, object]) -> None:
        """method to extract all links

        This method is responsible for extracting all the links from the page.
        After extracting the links, it will navigate to each link and extract the data based on the action data provided to this method.
        Then it will store the data into database.
        After extracting data from all the links it will generate a csv file for the extracted data.

        Args:
            page: The playwright page object.
            action_data: The action data based on which actions will be performed.

        """

        logger.info("executing get_all_links command...")
        links = await page.query_selector_all(action_data['selector'])
        urls = await page.evaluate('(links) => links.map(a => a.href)', links)
        logger.info(f'Found {len(urls)} links')
        unique_list = pd.Series(urls).drop_duplicates().tolist()
        logger.info(f'Found {len(unique_list)} unique links')
        data_collection_instance = DataCollection()
        action_instance = action_executor.ActionExecutor()
        # for url in unique_list[:10]:  # for testing 
        for url in unique_list:
            page.set_default_timeout(30000)
            try:
                await page.goto(url)
            except Exception as _:
                logger.error(f"Failed to load url: {url}", exc_info=True)
                continue
            page.set_default_timeout(2000)
            # create a new row which is a empty dictionary to store all the values extracted from the page.
            with data_store_context_for_every_page() as new_row:
                new_row['ProductURL'] = url
                new_row['Company_Name'] = action_data['companyName']
                new_row['Country_Name'] = action_data['countryName']
                new_row['Currency'] = action_data['currency']
                for page_action_data in action_data['pageActions']:
                    try:
                        await action_instance.action(page, page_action_data, new_row)
                    except Exception as _:
                        logger.error(f"Action failed for url: {url} while extracting {page_action_data['key']}", exc_info=True)
                        continue
            data_collection_instance.add_row(new_row)
            record_df = pd.DataFrame([new_row])
            # push the record to database
            record_df.to_sql("ornament", con=engine, index=False, if_exists="append")
            logger.info("record pushed to database successfully")
            # dispatch(
            #     "cat-requested-a-fish",  # Event name, accepts any valid string
            #     payload={"cat_id": "fd375d23-b0c9-4271-a9e0-e028c4cd7230","data": new_row}, middleware_id=7
            # )
        # generate the csv file after completion of extracting data from all the links of a company.
        data_collection_instance.get_df(f"{action_data['companyName']}")