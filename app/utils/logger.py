from __future__ import annotations

import json
import logging
from sys import stdout
from typing import Any, Mapping

from loguru import logger

from app.utils.config import settings


def serialize(record: Mapping[str, Any]) -> str:
    subset = {
        "timestamp": record["time"].utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "message": record["message"],
        "level": record["level"].name,
        "context": {
            "service": settings.APP_NAME,
            "process": {"id": record["process"].id, "name": record["process"].name},
            "thread": {"id": record["thread"].id, "name": record["thread"].name},
            "file": record["file"].path,
            "function": record["function"],
            "line": record["line"],
        },
    }
    return json.dumps(subset)


def patching(record: Mapping[str, Any]) -> None:
    record["extra"]["serialized"] = serialize(record)


class CustomLogger:
    def __init__(self, level: int, is_dev: bool) -> None:
        logger.remove(0)
        logging.basicConfig(level=level)

        if not is_dev:
            self._logger: Any = logger.patch(patching)
            self._logger.add(stdout, level=level, format="{extra[serialized]}", backtrace=True)
        else:
            self._logger = logger.bind(service=settings.APP_NAME)
            self._logger.add(
                stdout,
                level=level,
                format="{time:HH:mm:ss:SSSS!UTC} | {name} | {level} | {file.name}:{line} | {message}",
                backtrace=True,
            )

    def get_instance(self) -> Any:
        return self._logger


log: Any = CustomLogger(
    level=logging.getLevelName(settings.LOGGING_LEVEL), is_dev=settings.IS_DEV
).get_instance()
