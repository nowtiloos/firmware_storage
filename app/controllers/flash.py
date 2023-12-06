from fastapi import APIRouter, UploadFile, Depends

from app.schemas.flash import SFlash, FlashSearch

router: APIRouter = APIRouter(prefix="/flash", tags=["Upload/Download flash"])


@router.post(path="/upload")
async def upload_flash(file: UploadFile,
                       flash: SFlash):
    ...


@router.get("")
async def get_flash(search_args: FlashSearch = Depends()):
    ...