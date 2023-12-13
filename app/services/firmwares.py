from app.interfaces.unit_of_work import IUnitOfWork
from app.schemas.firmware import SNewFirmware


class FirmwareServices:
    def __init__(self, unit_of_work: IUnitOfWork) -> None:
        self.unit_of_work = unit_of_work

    async def add_firmwares(self, upload_firmware: SNewFirmware):
        async with self.unit_of_work as uow:
            new_firmware = await uow.firmwares.add(upload_firmware.model_dump())
            return new_firmware
