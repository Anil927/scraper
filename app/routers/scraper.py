from fastapi import APIRouter, Depends
import asyncio

from app.service_impl.website_scraper import main


router = APIRouter()

@router.post("/route")
def scrape(files: list[str]) -> None:
    asyncio.run(main(files))
