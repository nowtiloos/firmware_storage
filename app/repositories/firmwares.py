from app.interfaces.repository import IFirmwaresRepository
from app.models.firmwares import Firmwares
from app.repositories.base_repository import SQLAlchemyRepository


class FirmwaresRepository(SQLAlchemyRepository, IFirmwaresRepository):
    model = Firmwares
