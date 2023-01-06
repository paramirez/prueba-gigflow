""" Module containing the `Delivery` domain model class. """
from pydantic import BaseModel


class Delivery(BaseModel):
    """ 
    Class representing a delivery.

    Attributes:
        id (int): Unique identifier for the delivery.
        name (str): Name of the delivery.
    """
    id: int
    name: str
