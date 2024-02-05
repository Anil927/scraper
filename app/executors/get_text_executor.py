from playwright.async_api import Playwright
import re

from app.executors.executor_interface import ExecutorInterface
from app.actions.locator import locate

class GetTextExecutor(ExecutorInterface):

    async def execute(self, page: Playwright, action_data: dict[str, object], store: dict | None=None) -> None:
        element = locate(page, action_data)
        text = await element.inner_text()
        text = text.strip()
        if action_data.get('transform', None) is not None:
            if action_data['transform']['type'] == 'lambda':
                transformer= eval(action_data['transform']['value'])
                store[action_data['key']]=transformer(text)
            elif action_data['transform']['type'] == 'regex':
                pattern_match = re.search(action_data['transform']['pattern'], text)
                store[action_data['key']] = pattern_match.group()
        else:
            store[action_data['key']]=text