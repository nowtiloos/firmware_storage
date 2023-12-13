from fastapi import Depends

from app.dependices.unit_of_work import get_unit_of_work
from app.interfaces.unit_of_work import IUnitOfWork
from app.services.firmwares import FirmwareServices


def get_firmwares_services(unit_of_work: IUnitOfWork = Depends(get_unit_of_work)) -> FirmwareServices:
    return FirmwareServices(unit_of_work)
