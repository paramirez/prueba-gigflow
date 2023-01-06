"""
Module containing the rest api declaration routes and app
"""
from fastapi import FastAPI, Depends
from .database import get_session
from ..prueba.infrastructure.sqlalchemy.adapters.sqlalchemy_service_repository import SQLAlchemyServiceRepository
from ..prueba.application.use_cases.service_finder import find_all_services, find_service_by_id

app = FastAPI()


@app.get(path='/services')
def get_all_services(db_session=Depends(get_session)):
    """
    Route handler for retrieving a list of all services.

    Returns:
        List[Service]: A list of `Service` objects.
    """
    repository = SQLAlchemyServiceRepository(db_session)
    return find_all_services(repository)


@app.get(path='/services/{service_id}')
def get_all_service_by_id(service_id: int, db_session=Depends(get_session)):
    """
    Route handler for retrieving a service by its ID.

    Args:
        service_id (int): The ID of the service to retrieve.

    Returns:
        Service: A `Service` object with the provided ID.
    """
    repository = SQLAlchemyServiceRepository(db_session)
    return find_service_by_id(repository, service_id=service_id)
