from abc import ABC

from app.models.modified_firmwares import ModifiedFirmwares
from app.utils.repository import SQLAlchemyRepository


class ModifiedFirmwaresRepository(SQLAlchemyRepository, ABC):
    model = ModifiedFirmwares
