from fastapi import APIRouter, Depends, UploadFile

from app.dependencies.auth import get_current_user
from app.dependencies.file_manager import get_firmware_folder
from app.dependencies.services import get_firmwares_services
from app.models.users import Users
from app.schemas.firmware import SFirmware
from app.services.file_manager import FileManager
from app.services.firmwares import FirmwareServices

router: APIRouter = APIRouter(prefix="/firmwares", tags=["Firmware Manager"])


@router.post(path="/upload_file", status_code=201)
async def upload_flash(file: UploadFile,
                       truck_model: str,
                       engine_model: str,
                       ecu_model: str,
                       flasher: str,
                       user: Users = Depends(get_current_user),
                       file_manager: FileManager = Depends(get_firmware_folder),
                       firmware_services: FirmwareServices = Depends(get_firmwares_services)):
    file_path: str = await file_manager.save_uploaded_file(file=file)

    upload_firmware: SFirmware = SFirmware(file_name=file.filename,
                                           truck_model=truck_model,
                                           engine_model=engine_model,
                                           ecu_model=ecu_model,
                                           flasher=flasher,
                                           file_path=file_path,
                                           file_size=file.size,
                                           user_uploaded=user.name)
    return await firmware_services.add_firmwares(upload_firmware)


@router.get("")
async def get_flash(firmware_services: FirmwareServices = Depends(get_firmwares_services)) -> list[SFirmware]:
    search = await firmware_services.search_firmwares()
    return search
