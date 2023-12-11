from fastapi import APIRouter

from app.schemas.firmware import SFirmware

router: APIRouter = APIRouter(prefix="/flash", tags=["Upload/Download flash"])


@router.post(path="/upload")
async def upload_flash(firmware: SFirmware):
    ...


@router.get("")
async def get_flash():
    ...

