import asyncio
import json
import time

from app.service_impl.base_scraper import BaseScraper
from app.actions.action_executor import ActionExecutor
from app.logger_utils.logger import logger


class WebsiteScraper(BaseScraper):
    """ 
    WebsiteScraper class is used to scrape the website based on the json configuration file.
    """

    def __init__(self, config_file: str):
        """ 
        Constructor to initialize the WebsiteScraper class.

        Parameters:
            config_file: The path of the JSON configuration file for scraping the website.
        """
        super().__init__()
        with open(config_file) as f:
            self.config = json.load(f)
        self.action_instance = ActionExecutor()

    async def scrape(self) -> None:
        """ 
        Method to scrape the website based on the JSON configuration file.
        """
        page = await self.start()
        for action_data in self.config['actions']:
            await self.action_instance.action(page, action_data)
        await self.close()


async def main(files: list[str]) -> None:
    """ 
    Main method to scrape the websites based on the JSON configuration files.

    Parameters:
        files: The list of JSON configuration files for scraping the websites.
    """

    for website in files:
        start_time = int(time.time() * 1000)
        import main
        scraper = WebsiteScraper(f"./app/config/{website}")
        logger.info(
            f'Scraping started for Company: {website.split("/")[-1].split(".")[0]}')    
        try:
            await scraper.scrape()
        except Exception as _:
            logger.error(
                f'Scraping failed for Company: {website.split("/")[-1].split(".")[0]}', exc_info=True)
            continue
        finally:
            end_time = int(time.time() * 1000)
            logger.info(f'Time taken for scraping: {end_time - start_time} ms')
        logger.info(
            f'Scraping completed for Company: {website.split("/")[-1].split(".")[0]}')
