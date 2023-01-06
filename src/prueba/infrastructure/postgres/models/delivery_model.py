"""
Module containing a SQLAlchemy model class for representing a delivery.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence
from .base_model import BaseModel


class DeliveryModel(BaseModel):
    """
    SQLAlchemy model class for representing a delivery of a package of services.

    Attributes:
        id (int): ID of the delivery.
        packageID (int): ID of the package associated with the delivery.
        name (str): Name of the delivery.
    """
    __tablename__ = "deliveries"

    id = Column(Integer, Sequence('deliveries_id_seq'), primary_key=True)
    packageID = Column(Integer, ForeignKey("packages.id"))
    name = Column(String)
