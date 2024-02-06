from playwright.async_api import Playwright
import re

from app.executors.executor_interface import ExecutorInterface
from app.actions.locator import locate

class GetTextExecutor(ExecutorInterface):
    """class from extracting the text from the page."""

    async def execute(self, page: Playwright, action_data: dict[str, object], store: dict | None=None) -> None:
        """method to extract the text from the page.

        After extacting text from the page, it can transform the text using the transform key in the action_data.
        Then the data will be stored the data in the store.

        Args:
            page: The playwright page object.
            action_data: The action data to be executed.
            store: The store(a dictionary) to store the extracted data.

        Raises:
            KeyError: If the action_data does not contain the key named "key".
                      This is because we need a unique identifier for storing the data.
        """
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