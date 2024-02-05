from playwright.async_api import Playwright
import sys

from app.executors.get_text_executor import GetTextExecutor
from app.executors.get_link_executor import GetLinkExecutor
from app.executors.click_executor import ClickExecutor
from app.executors.get_all_links_executor import GetAllLinksExecutor
from app.executors.infinite_scroll_executor import InfiniteScrollExecutor
from app.executors.goto_url_executor import GotoUrlExecutor
from app.models.action_type import ActionType
from app.store.context_manager import data_store_context_for_every_page
from app.store.data_collection import DataCollection


class ActionExecutor:
    """ 
    This class is responsible for executing the action based on the action type.
    """

    def __init__(self):
        """ 
        Initilizes all the executors for each action type.
        """
        self.goto_url_executor = GotoUrlExecutor()
        self.infinite_scroll_executor = InfiniteScrollExecutor()
        self.click_executor = ClickExecutor()
        self.get_all_links_executor = GetAllLinksExecutor()
        self.get_text_executor = GetTextExecutor()
        self.get_link_executor = GetLinkExecutor()


    async def action(self, page: Playwright, action_data:  dict[str, object], store: dict | None=None) -> None:
        """ 
        Based on the action type, it will execute the action.
        """
        if action_data['actionType'] == ActionType.GOTO_URL.value:
            await self.goto_url_executor.execute(page, action_data)
        elif action_data['actionType'] == ActionType.INFINITE_SCROLL.value:
            await self.infinite_scroll_executor.execute(page, action_data)
        elif action_data['actionType'] == ActionType.GET_ALL_LINKS.value:
            await self.get_all_links_executor.execute(page, action_data)
        elif action_data['actionType'] == ActionType.CLICK.value:
            await self.click_executor.execute(page, action_data)
        elif action_data['actionType'] == ActionType.GET_LINK.value:
            await self.get_link_executor.execute(page, action_data, store)
        elif action_data['actionType'] == ActionType.GET_TEXT.value:
            await self.get_text_executor.execute(page, action_data, store)
        else:
            print("No action found")
            sys.exit(1)

