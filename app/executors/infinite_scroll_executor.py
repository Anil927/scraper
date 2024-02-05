import asyncio
from playwright.async_api import Playwright

from app.executors.executor_interface import ExecutorInterface
from app.actions.locator import locate
from app.executors.click_executor import ClickExecutor
from app.models.action_type import ActionType
from app.logger_utils.logger import logger


class InfiniteScrollExecutor(ExecutorInterface):

    async def execute(self, page: Playwright, action_data: dict[str, object]) -> None:
        # print("executing infinite_scroll command...")
        logger.info('executing infinite_scroll command')
        try:    
            if action_data.get("scroll_to", None) is not None:
                await page.mouse.wheel(scroll_to['x'], scroll_to['y'])
                return
            is_visible = False
            if action_data.get("scroll_to", None) is not None:
                is_visible = await locate(page, action_data["extra"]['condition']).is_visible()
            prev_height = 0
            consecutive_no_scroll_count = 0
            i = 0
            # while True:
            while i < 20:
                current_height = await page.evaluate('(window.innerHeight + window.scrollY)')
                if current_height == prev_height:
                    consecutive_no_scroll_count += 1
                    if consecutive_no_scroll_count >= 3: 
                        logger.info("Reached end of page")
                        break
                else:
                    consecutive_no_scroll_count = 0
                await self.scroll_page(page, action_data.get('selector', None), action_data['scrollHeight'])
                prev_height = current_height
                if is_visible and extra['actionType'] == ActionType.CLICK.value:
                    await ClickExecutor().execute(page, extra)
                i += 1
        except Exception as e:
            logger.error("error occurred while executing infinite_scroll command", e)

    async def scroll_page(self, page: Playwright, selector: str | None=None, scroll_height: int=100):
        if selector:
            if await page.locator(selector).is_visible() is False:
                await page.mouse.wheel(0, scroll_height)
            else:
                await page.locator(selector).click()
        else:
            await page.mouse.wheel(0, scroll_height)
        await asyncio.sleep(0.01)

            
            

        