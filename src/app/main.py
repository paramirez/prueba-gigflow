"""
Module containing the start function for running the API server.
"""
import uvicorn
from .config import get_settings

settings = get_settings()


def start():
    """
    Start the API server.

    The server is started using uvicorn and listens on the host and 
    port specified in the `APPSettings` object.
    """
    uvicorn.run(
        'src.app.api:app',
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
