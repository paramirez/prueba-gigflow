"""
Module containing a SQLAlchemy model class for representing a package.
"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class PackageModel(BaseModel):
    """
    SQLAlchemy model class for representing a package of services.

    Attributes:
        id (int): ID of the package.
        description (str): Description of the services included in the package.
        price (float): Price of the package.
        typeOfServiceID (int): ID of the type of service that the package belongs to.
        deliveries (list): List of deliveries associated with the package.
    """
    __tablename__ = "packages"

    id = Column(Integer, Sequence('packages_id_seq'), primary_key=True)
    description = Column(String)
    price = Column(Float)
    typeOfServiceID = Column(Integer, ForeignKey("services.id"))
    deliveries = relationship("DeliveryModel", cascade="all, delete-orphan")
