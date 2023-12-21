from app.interfaces.unit_of_work import IUnitOfWork
from app.schemas.firmware import SFirmware


class FirmwareServices:
    def __init__(self, unit_of_work: IUnitOfWork) -> None:
        self.unit_of_work = unit_of_work

    async def add_firmwares(self, upload_firmware: SFirmware):
        async with self.unit_of_work as uow:
            await uow.firmwares_repository.add(**upload_firmware.model_dump())
            return {"message": "Файл загружен на сервер"}

    async def search_all_firmwares(self):
        async with self.unit_of_work as uow:
            return await uow.firmwares_repository.find_all()

    async def search_firmwares_by_filter(self, **kwargs):
        async with self.unit_of_work as uow:
            filers: dict = {key: value for key, value in kwargs.items() if value}
            return await uow.firmwares_repository.find_by_filter(**filers)
