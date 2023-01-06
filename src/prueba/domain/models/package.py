""" Module containing the `Package` domain model class. """
from typing import List
from pydantic import BaseModel
from .delivery import Delivery


class Package(BaseModel):
    """
    Class representing a package of services offered by a freelance.

    Attributes:
        id (int): Unique identifier for the package.
        typeOfServiceID (int): ID of the type of service that the package belongs to.
        description (str): Description of the services included in the package.
        price (int): Price of the package.
        deliveries (List[Delivery]): List of deliveries associated with the package.
    """
    id: int
    typeOfServiceID: int
    description: str
    price: int
    deliveries: List[Delivery]
