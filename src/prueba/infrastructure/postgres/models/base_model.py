"""
Module containing the `BaseModel` class, which serves as a base class for SQLAlchemy models.
"""
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    """
    Base class for creating SQLAlchemy model classes.
    """
    __abstract__ = True
