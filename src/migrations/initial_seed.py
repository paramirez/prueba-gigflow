from src.app.database import get_session

from src.prueba.infrastructure.sqlalchemy.models import ServiceModel
from src.prueba.infrastructure.sqlalchemy.models import PackageModel
from src.prueba.infrastructure.sqlalchemy.models import DeliveryModel


def run():
    session = next(get_session())
    session.add(ServiceModel(
        name="Service 1"
    ))
    session.commit()
    session.add(PackageModel(
        description="Lorem ipsum dolor sit amet, consectetur adipiscing eli",
        price=100,
        typeOfServiceID=1
    ))
    session.commit()
    session.add(DeliveryModel(
        name="Delivery 1",
        packageID=1
    ))
    session.commit()
    session.add(DeliveryModel(
        name="Delivery 2",
        packageID=1
    ))
    session.commit()
