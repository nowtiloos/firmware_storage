from abc import ABC

from app.models.firmware_calibrators import FirmwareCalibrators
from app.utils.repository import SQLAlchemyRepository


class FirmwareCalibratorsRepository(SQLAlchemyRepository, ABC):
    model = FirmwareCalibrators
