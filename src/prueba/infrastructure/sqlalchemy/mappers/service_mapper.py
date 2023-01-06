"""
Module containing a class for mapping `Service` domain
objects to/from `ServiceModel` database model objects.
"""
from ....domain.models.service import Service
from ..models.service_model import ServiceModel
from .package_mapper import PackageMapper


class ServiceMapper:
    """
    ServiceMapper is a class for mapping `Service`
    domain objects to/from `ServiceModel` database model objects.
    """

    def __init__(self) -> None:
        self.__package_mapper = PackageMapper()

    def map_model_to_domain(self, service_model: ServiceModel) -> Service:
        """
        Map a `ServiceModel` object to a `Service` object.

        Args:
            service_model (ServiceModel): The `ServiceModel` object to map.

        Returns:
            Service: The resulting `Service` object.
        """
        return Service(
            id=service_model.id,
            name=service_model.name,
            packages=[
                self.__package_mapper.map_model_to_domain(package_model)
                for package_model in service_model.packages
            ]
        )

    def map_domain_to_model(self, service: Service) -> ServiceModel:
        """
        Map a `Service` object to a `ServiceModel` object.

        Args:
            service (Service): The `Service` object to map.

        Returns:
            ServiceModel: The resulting `ServiceModel` object.
        """
        return ServiceModel(
            id=service.id,
            name=service.name
        )
