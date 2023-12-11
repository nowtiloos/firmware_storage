from abc import ABC

from app.models.firmwares import Firmwares
from app.utils.repository import SQLAlchemyRepository


class FirmwaresRepository(SQLAlchemyRepository, ABC):
    model = Firmwares
