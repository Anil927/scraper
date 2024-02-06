from playwright.async_api import Playwright

from app.actions.locator import locate
from app.executors.executor_interface import ExecutorInterface


class GetLinkExecutor(ExecutorInterface):
    """This class is responsible for extracting the link from the page."""

    async def execute(self, page: Playwright, action_data: dict[str, object], store: dict | None=None) -> None:
        """method to extract the link from the page.
        
        Usually used to extract the link for images or other media files i.e. the 'src' attribute of the element.

        Args:
            page: The playwright page object.
            action_data: The action data to be executed.
            store: The store(a dictionary) to store the extracted data.

        Raises :
            KeyError: If the action_data does not contain the key named "key".
                      This is because we need a unique identifier for storing the data.
        """

        element = locate(page, action_data)
        src = await element.get_attribute('src')
        store[action_data['key']] = src
       