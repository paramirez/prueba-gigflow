"""
Module containing a class for mapping `Delivery` domain
objects to/from `DeliveryModel` database model objects.
"""
from ..models.delivery_model import DeliveryModel
from ....domain.models.delivery import Delivery


class DeliveryMapper:
    """
    DeliveryMapper is a class for mapping `Delivery` domain 
    objects to/from `DeliveryModel` database model objects.
    """

    def map_model_to_domain(self, delivery_model: DeliveryModel) -> Delivery:
        """
        Map a `DeliveryModel` object to a `Delivery` object.

        Args:
            delivery_model (DeliveryModel): The `DeliveryModel` object to map.

        Returns:
            Delivery: The resulting `Delivery` object.
        """
        return Delivery(
            id=delivery_model.id,
            name=delivery_model.name
        )

    def map_domain_to_model(self, delivery: Delivery) -> DeliveryModel:
        """
        Map a `Delivery` object to a `DeliveryModel` object.

        Args:
            delivery (Delivery): The `Delivery` object to map.

        Returns:
            DeliveryModel: The resulting `DeliveryModel` object.
        """
        return DeliveryModel(
            id=delivery.id,
            name=delivery.name
        )
