"""
Module containing a class that extends the `ServiceRepository` interface.

This module contains the `SQLAlchemyServiceRepository` class, which implements
the methods defined in `ServiceRepository` using a SQLAlchemy. It is responsible for retrieving and
manipulating `Service` objects from the database.
"""
from typing import List
from sqlalchemy.orm.session import Session
from ....domain.ports.service_repository import ServiceRepository
from ....domain.models.service import Service
from ..models.service_model import ServiceModel
from ..mappers.service_mapper import ServiceMapper


class SQLAlchemyServiceRepository(ServiceRepository):
    """
    SQLAlchemyServiceRepository is a class that extends the `ServiceRepository` interface.
    """

    def __init__(self, session: Session) -> None:
        self.__session = session
        self.__mapper = ServiceMapper()

    def get_service_by_id(self, service_id: int) -> Service:
        """
        :ref:`ServiceRepository.get_service_by_id`
        """
        row = self.__session.query(ServiceModel).get(service_id)
        if row is None:
            return None
        return self.__mapper.map_model_to_domain(service_model=row)

    def get_all_services(self) -> List[Service]:
        """
        :ref:`ServiceRepository.get_all_services`
        """
        rows = self.__session.query(ServiceModel).all()
        return list(map(self.__mapper.map_domain_to_model, rows))
