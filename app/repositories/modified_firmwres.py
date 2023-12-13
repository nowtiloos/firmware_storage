from app.interfaces.repository import IModifiedFirmwaresRepository
from app.models.modified_firmwares import ModifiedFirmwares
from app.repositories.base_repository import SQLAlchemyRepository


class ModifiedFirmwaresRepository(SQLAlchemyRepository, IModifiedFirmwaresRepository):
    model = ModifiedFirmwares
