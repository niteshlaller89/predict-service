from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.v1 import router as api_router
from app.utils.config import settings
from app.utils.logger import log


def get_application() -> FastAPI:
    application: FastAPI = FastAPI(title=settings.APP_NAME, debug=True, version=settings.VERSION)
    application.include_router(health_router)
    application.include_router(api_router, prefix=settings.API_PREFIX)

    log.info(f"App: {settings.APP_NAME} initialized...")
    log.info(f"Settings: {settings.model_dump_json()}")
    return application


app: FastAPI = get_application()
