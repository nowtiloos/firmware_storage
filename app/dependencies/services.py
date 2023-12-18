from fastapi import Depends

from app.dependencies.unit_of_work import get_unit_of_work
from app.interfaces.unit_of_work import IUnitOfWork
from app.services.auth import AuthServices
from app.services.firmwares import FirmwareServices


def get_firmwares_services(unit_of_work: IUnitOfWork = Depends(get_unit_of_work)) -> FirmwareServices:
    return FirmwareServices(unit_of_work)


def get_auth_services(unit_of_work: IUnitOfWork = Depends(get_unit_of_work)) -> AuthServices:
    return AuthServices(unit_of_work)
