"""
Module containing a class for mapping `Package` domain
objects to/from `PackageModel` database model objects.
"""
from ....domain.models.package import Package
from ..models.package_model import PackageModel
from .delivery_mapper import DeliveryMapper


class PackageMapper:
    """
    PackageMapper is a class for mapping `Package` domain
    objects to/from `PackageModel` database model objects.
    """

    def __init__(self) -> None:
        self.__delivery_mapper = DeliveryMapper()

    def map_model_to_domain(self, package_model: PackageModel) -> Package:
        """
        Map a `PackageModel` object to a `Package` object.

        Args:
            package_model (PackageModel): The `PackageModel` object to map.

        Returns:
            Package: The resulting `Package` object.
        """
        return Package(
            id=package_model.id,
            typeOfServiceID=package_model.typeOfServiceID,
            description=package_model.description,
            price=package_model.price,
            deliveries=[
                self.__delivery_mapper.map_model_to_domain(delivery_model)
                for delivery_model in package_model.deliveries
            ]
        )

    def map_domain_to_model(self, package: Package) -> PackageModel:
        """
        Map a `Package` object to a `PackageModel` object.

        Args:
            package (Package): The `Package` object to map.

        Returns:
            PackageModel: The resulting `PackageModel` object.
        """
        return PackageModel(
            id=package.id,
            typeOfServiceID=package.typeOfServiceID,
            description=package.description,
            price=package.price
        )
