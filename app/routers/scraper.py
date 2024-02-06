from fastapi import APIRouter, Depends
import asyncio

from app.service_impl.website_scraper import main


router = APIRouter()

@router.post("/route")
def scrape(files: list[str]) -> None:
    """This function is responsible for scraping the website.
    
    Args:
        files: The list of files(json configuration files for various websites) to be scraped.

    """
    asyncio.run(main(files))
