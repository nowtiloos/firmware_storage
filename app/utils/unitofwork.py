from abc import ABC, abstractmethod
from typing import Type

from app.database.database import async_session_maker
from app.repositories.firmware_calibrators import FirmwareCalibratorsRepository
from app.repositories.firmwares import FirmwaresRepository
from app.repositories.modified_firmwres import ModifiedFirmwaresRepository
from app.repositories.users import UsersRepository


class IUnitOfWork(ABC):
    firmware_calibrators: Type[FirmwareCalibratorsRepository]
    firmwares: Type[FirmwaresRepository]
    modified_firmwares: Type[ModifiedFirmwaresRepository]
    users: Type[UsersRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.firmware_calibrators = FirmwareCalibratorsRepository(self.session)
        self.firmwares = FirmwaresRepository(self.session)
        self.modified_firmwares = ModifiedFirmwaresRepository(self.session)
        self.users = UsersRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
