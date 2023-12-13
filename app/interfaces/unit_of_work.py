from abc import ABC, abstractmethod
from types import TracebackType

from app.repositories.firmware_calibrators import FirmwareCalibratorsRepository
from app.repositories.firmwares import FirmwaresRepository
from app.repositories.modified_firmwres import ModifiedFirmwaresRepository
from app.repositories.users import UsersRepository


class IUnitOfWork(ABC):
    firmware_calibrators: FirmwareCalibratorsRepository
    firmwares: FirmwaresRepository
    modified_firmwares: ModifiedFirmwaresRepository
    users: UsersRepository

    @abstractmethod
    async def __aenter__(self) -> "IUnitOfWork":
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type: BaseException | None, exc_val: BaseException | None,
                        exc_tb: TracebackType | None) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError
