from playwright.async_api import Playwright

from app.executors.executor_interface import ExecutorInterface


class GotoUrlExecutor(ExecutorInterface):
    """This class is responsible for navigating to the url."""

    async def execute(self, page: Playwright, action_data: dict[str, object]) -> None:
        """This method is responsible for navigating to the url.

        Args:
            page: The playwright page object.
            action_data: The action data to be executed.
                It must contain a "url" key with the target URL as value.
                
        Raises:
            KeyError: If the action_data does not contain the "url" key.
        """
        await page.goto(action_data['url'])