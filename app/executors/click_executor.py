from playwright.async_api import Playwright

from app.executors.executor_interface import ExecutorInterface
from app.actions.locator import locate


class ClickExecutor(ExecutorInterface):
    
    async def execute(self, page: Playwright, action_data: dict[str, object]) -> None:
        await locate(page, action_data).click()
        
        