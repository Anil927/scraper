from playwright.async_api import Playwright

from app.executors.executor_interface import ExecutorInterface
from app.actions.locator import locate


class ClickExecutor(ExecutorInterface):
    """This class is responsible for executing the click action."""
    
    async def execute(self, page: Playwright, action_data: dict[str, object]) -> None:
        """This method is responsible for executing the click action.

        Args:
            page: The playwright page object.
            action_data: The action data to be executed.
        """
        
        await locate(page, action_data).click()
        
        