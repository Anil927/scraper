"""This Method contains the BaseScraper class that is used to initilize and close the playwright and the browser """

import asyncio
from playwright.async_api import async_playwright, Playwright

class BaseScraper:
    """ 
    Base class for the scraper.
    """

    def __init__(self) -> None:
        """ 
        Initializes the playwright, browser.
        """
        self.playwright = None
        self.browser = None

    async def start(self) -> Playwright:
        """
        Method to start the browser and return the page.
        """
        # Initialize playwright
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.page = await self.browser.new_page()
        return self.page

    async def close(self) -> None:
        """
        Close method that closes the browser when done scraping.
        """
        await self.browser.close()
        await self.playwright.stop()

