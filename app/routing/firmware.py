from fastapi import APIRouter, Depends

from app.dependices.services import get_firmwares_services
from app.schemas.firmware import SFirmwareSearch, SNewFirmware
from app.services.firmwares import FirmwareServices

router: APIRouter = APIRouter(prefix="/flash", tags=["Upload/Download flash"])


@router.post(path="/upload")
async def upload_flash(firmware: SNewFirmware, firmware_services: FirmwareServices = Depends(get_firmwares_services)):
    new_firmware = await firmware_services.add_firmwares(upload_firmware=firmware)
    return new_firmware


@router.get("")
async def get_flash(query: SFirmwareSearch):
    ...
