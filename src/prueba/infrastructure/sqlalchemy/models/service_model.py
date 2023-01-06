"""
Module containing a SQLAlchemy model class for representing a service.
"""
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class ServiceModel(BaseModel):
    """
    SQLAlchemy model class for representing a service.

    Attributes:
        id (int): ID of the service.
        name (str): Name of the service.
        packages (list): List of packages associated with the service.
    """

    __tablename__ = "services"

    id = Column(Integer, Sequence('services_id_seq'), primary_key=True)
    name = Column(String)
    packages = relationship("PackageModel", cascade="all, delete-orphan")
