from playwright.async_api import Playwright

from app.executors.executor_interface import ExecutorInterface


class GotoUrlExecutor(ExecutorInterface):

    async def execute(self, page: Playwright, action_data: dict[str, object]) -> None:
        await page.goto(action_data['url'])