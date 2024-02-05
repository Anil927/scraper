from playwright.async_api import Playwright

from app.actions.locator import locate
from app.executors.executor_interface import ExecutorInterface


class GetLinkExecutor(ExecutorInterface):

    async def execute(self, page: Playwright, action_data: dict[str, object], store: dict | None=None) -> None:
        element = locate(page, action_data)
        src = await element.get_attribute('src')
        store[action_data['key']] = src
       