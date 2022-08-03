# ../../project/app/config.py

import logging
import os
from functools import lru_cache

from pydantic import BaseConfig, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config seetings from the environment...")
    return Settings()
