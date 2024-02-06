from abc import ABC, abstractmethod
from playwright.sync_api import Playwright

class ExecutorInterface(ABC):
    """This class is an interface for the executor classes."""

    @abstractmethod
    def execute(self, page: Playwright, action_data: dict[str, object]) -> None:
        pass