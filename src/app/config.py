"""
Module containing the APPSettings class.

This class represents the application's configuration settings, which can be
loaded from a .env file or specified as environment variables.
"""
from pydantic import BaseSettings
from functools import lru_cache


class APPSettings(BaseSettings):
    """
    Configuration class for the application.
    """
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    DATABASE_URL: str

    class Config:
        """Inner class for specifying configuration loading options."""
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    """
    Returns:
        APPSettings: The resulting `APPSettings` object.
    """
    return APPSettings()
