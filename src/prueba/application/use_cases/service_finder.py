"""
Module containing functions for finding `Service` objects using a `ServiceRepository`.
"""
from typing import List
from ...domain.ports.service_repository import ServiceRepository
from ...domain.models.service import Service


def find_service_by_id(service_repository: ServiceRepository, service_id: int) -> Service:
    """
    Find a `Service` object by ID using a `ServiceRepository`.

    Args:
        service_repository (ServiceRepository): The `ServiceRepository` to use for finding the service.
        service_id (int): The ID of the service to find.

    Returns:
        Service: The `Service` domain object with the given ID.
    """
    return service_repository.get_service_by_id(service_id)


def find_all_services(service_repository: ServiceRepository) -> List[Service]:
    """
    Find all `Service` objects using a `ServiceRepository`.

    Args:
        service_repository (ServiceRepository): The `ServiceRepository` to use for finding the services.

    Returns:
        List[Service]: A list of all `Service` objects.
    """
    return service_repository.get_all_services()
