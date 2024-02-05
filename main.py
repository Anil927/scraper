from fastapi import FastAPI
from fastapi_events.middleware import EventHandlerASGIMiddleware
from fastapi_events.handlers.local import local_handler
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.routers import scraper
from app.models import models
from app.database_config import database

app = FastAPI()
# event_handler_id: int = 7
# app.add_middleware(EventHandlerASGIMiddleware, handlers=[local_handler], middleware_id=event_handler_id)
static_directory = Path(__file__).resolve().parent / "app/config"
app.mount("/app/config", StaticFiles(directory="app/config"), name="config")
app.include_router(scraper.router)

models.Base.metadata.create_all(bind=database.engine)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)