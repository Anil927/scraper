import asyncio
from playwright.async_api import Playwright

from app.executors.executor_interface import ExecutorInterface
from app.actions.locator import locate
from app.executors.click_executor import ClickExecutor
from app.models.action_type import ActionType
from app.logger_utils.logger import logger


class InfiniteScrollExecutor(ExecutorInterface):
    """A class to scroll a webpage infinitely."""

    async def execute(self, page: Playwright, action_data: dict[str, object]) -> None:
        """This method is responsible for scrolling the page infinitely.

        It can scroll the page infinitely until the end of the page or until a certain condition is met.
        It can also scroll to a certain element on the page or a certain height.

        Args:
            page: The playwright page object.
            action_data: The action data to be executed.

        """

        logger.info('executing infinite_scroll command')
        try:    
            # for scrolling to a certain height either horizontally or vertically
            if action_data.get("scroll_to", None) is not None:
                await page.mouse.wheel(scroll_to['x'], scroll_to['y'])
                return
            prev_height = 0
            consecutive_no_scroll_count = 0
            # i = 0  # for testing
            while True:
            # while i < 20:  # for testing
                is_visible = False 

                # extra may be used for locating and closing popups
                # for locating the element to be clicked in extra part like close button for popups
                if action_data.get("extra", None) is not None:
                    is_visible = await locate(page, action_data["extra"]).is_visible()
                if is_visible and extra['actionType'] == ActionType.CLICK.value:
                    await ClickExecutor().execute(page, action_data['extra'])
                total_page_height = await page.evaluate("document.body.scrollHeight")
                if total_page_height == prev_height:
                    consecutive_no_scroll_count += 1
                    if consecutive_no_scroll_count >= 3: 
                        logger.info("Reached end of page")
                        break
                else:
                    consecutive_no_scroll_count = 0
                scroll_height = (total_page_height - action_data['footerHeight']) if action_data.get('footerHeight', None) else 100
                logger.info(f"scrolling by {scroll_height}")
                await self.scroll_page(page, scroll_height, action_data.get('selector', None))
                await asyncio.sleep(action_data['pauseTimeInSec'])
                prev_height = total_page_height
                # i += 1  # for testing
        except Exception as e:
            logger.error("error occurred while executing infinite_scroll command", e)

    async def scroll_page(self, page: Playwright, scroll_height: int, selector: str | None=None):
        if selector:
            if await page.locator(selector).is_visible() is False:
                await page.evaluate(f"window.scrollTo(0, {scroll_height});")
            else:
                await page.locator(selector).click()
        else:
            await page.evaluate(f"window.scrollTo(0, {scroll_height});")

            
            

        