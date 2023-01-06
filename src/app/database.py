"""
Module containing the connectio and the get_session generator function.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URL, connect_args={
                       "check_same_thread": False})

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    """
    Generator function for creating and yielding a new database session.
    Yields:
        Session: A new database session.

    Example:
        >>> with get_session() as db_session:
        ...     # Use the database session here
        ...     pass
        >>> # The session is closed when the generator is closed.
    """
    db_session = session()
    try:
        yield db_session
    finally:
        db_session.close()
