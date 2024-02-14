from api.health import router as health_router
from api.v1 import router as api_router
from fastapi import FastAPI
from utils.events import create_start_app_handler

from app.utils.config import settings


def get_application() -> FastAPI:
    application = FastAPI(title=settings.APP_NAME, debug=True, version=settings.VERSION)
    application.include_router(health_router)
    application.include_router(api_router, prefix=settings.API_PREFIX)
    pre_load = False
    if pre_load:
        application.add_event_handler("startup", create_start_app_handler())  # type: ignore
    return application


app: FastAPI = get_application()
