""" Module containing the `ServiceRepository` interface. """
from typing import List
from abc import ABC, abstractmethod
from ..models.service import Service


class ServiceRepository(ABC):
    """
    Interface for a repository for storing and retrieving `Service` objects.
    """
    @abstractmethod
    def get_service_by_id(self, service_id: int) -> Service:
        """
        Retrieve a single `Service` domain model object from the repository.

        Args:
            service_id (int): ID of the service to retrieve.

        Returns:
            Service: The `Service` object with the given ID.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_all_services(self) -> List[Service]:
        """
        Retrieve a list of all `Service` domain model objects from the repository.

        Returns:
            List[Service]: A list of all `Service` domain model objects in the repository.
        """
        raise NotImplementedError()
