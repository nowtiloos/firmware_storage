from app.interfaces.repository import IFirmwareCalibratorsRepository
from app.models.firmware_calibrators import FirmwareCalibrators
from app.repositories.base_repository import SQLAlchemyRepository


class FirmwareCalibratorsRepository(SQLAlchemyRepository, IFirmwareCalibratorsRepository):
    model = FirmwareCalibrators
