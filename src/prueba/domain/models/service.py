""" Module containing the `Service` domain model class. """
from typing import List
from pydantic import BaseModel
from .package import Package


class Service(BaseModel):
    """
    Class representing a service offered by a freelancers.

    Attributes:
        id (int): Unique identifier for the service.
        name (str): Name of the service.
        packages (List[Package]): List of packages associated with the service.
    """
    id: int
    name: str
    packages: List[Package]