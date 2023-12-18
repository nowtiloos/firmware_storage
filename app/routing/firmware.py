from fastapi import APIRouter, Depends

from app.dependencies.services import get_firmwares_services
from app.schemas.firmware import SFirmwareSearch, SNewFirmware
from app.services.firmwares import FirmwareServices

router: APIRouter = APIRouter(prefix="/firmwares", tags=["Upload/Download flash"])


@router.post(path="/upload")
async def upload_flash(firmware: SNewFirmware,
                       file_path: str,
                       user_uploaded: str,
                       firmware_services: FirmwareServices = Depends(get_firmwares_services)):
    await firmware_services.add_firmwares(upload_firmware=firmware)


@router.get("")
async def get_flash(firmware_services: FirmwareServices = Depends(get_firmwares_services)):
    search = await firmware_services.search_firmwares()
    return search
