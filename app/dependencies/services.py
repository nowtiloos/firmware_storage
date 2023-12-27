from fastapi import Depends

from app.dependencies.unit_of_work import get_unit_of_work
from app.interfaces.unit_of_work import IUnitOfWork
from app.services.auth import AuthServices
from app.services.firmwares import FirmwareServices
from app.services.modified_firmwares import ModifiedFirmwareServices
from app.services.users import UsersServices


def get_firmwares_services(unit_of_work: IUnitOfWork = Depends(get_unit_of_work)) -> FirmwareServices:
    return FirmwareServices(unit_of_work)


def get_modified_firmwares_services(unit_of_work: IUnitOfWork = Depends(get_unit_of_work)) -> ModifiedFirmwareServices:
    return ModifiedFirmwareServices(unit_of_work)


def get_auth_services(unit_of_work: IUnitOfWork = Depends(get_unit_of_work)) -> AuthServices:
    return AuthServices(unit_of_work)


def get_users_services(unit_of_work: IUnitOfWork = Depends(get_unit_of_work)) -> UsersServices:
    return UsersServices(unit_of_work)
