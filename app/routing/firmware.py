from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user_with_access_to_write, get_current_user_with_access_to_read
from app.dependencies.file_manager import get_firmware_folder
from app.dependencies.services import get_firmwares_services
from app.models.users import Users
from app.schemas.firmware import SFirmware, FirmwareSearchDTO, UploadFirmwareDTO
from app.services.file_manager import FileManager
from app.services.firmwares import FirmwareServices

router: APIRouter = APIRouter(prefix="/firmwares", tags=["Firmware Manager"])


@router.post(path="/upload_file", status_code=201)
async def upload_firmware(
        upload_file: UploadFirmwareDTO = Depends(UploadFirmwareDTO),
        user: Users = Depends(get_current_user_with_access_to_write),
        file_manager: FileManager = Depends(get_firmware_folder),
        firmware_services: FirmwareServices = Depends(get_firmwares_services)
):
    file_path: str = await file_manager.save_uploaded_file(file=upload_file.file)
    firmware: SFirmware = SFirmware(file_name=upload_file.file.filename,
                                    truck_model=upload_file.truck_model,
                                    engine_model=upload_file.engine_model,
                                    ecu_model=upload_file.ecu_model,
                                    flasher=upload_file.flasher,
                                    file_path=file_path,
                                    file_size=upload_file.file.size,
                                    user_uploaded=user.name)
    return await firmware_services.add_firmwares(firmware)


@router.get("")
async def get_all_firmwares(
        firmware_services: FirmwareServices = Depends(get_firmwares_services),
        user: Users = Depends(get_current_user_with_access_to_read)
) -> list[SFirmware] | None:
    return await firmware_services.search_all_firmwares() if user else None


@router.get("/search")
async def search_firmware(
        search_form: FirmwareSearchDTO = Depends(FirmwareSearchDTO),
        firmware_services: FirmwareServices = Depends(get_firmwares_services),
        user: Users = Depends(get_current_user_with_access_to_read)
) -> list[SFirmware] | None:
    return await firmware_services.search_firmwares_by_filter(**search_form.model_dump()) if user else None
