from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user_with_access_to_read
from app.dependencies.services import get_modified_firmwares_services
from app.models.users import Users
from app.schemas.modified_firmwares import SModifiedFirmwares
from app.services.modified_firmwares import ModifiedFirmwareServices

router: APIRouter = APIRouter(prefix="/modified_firmwares", tags=["Modified firmwares"])


@router.get("/all")
async def get_all_firmwares(
        firmware_services: ModifiedFirmwareServices = Depends(get_modified_firmwares_services),
        user: Users = Depends(get_current_user_with_access_to_read)
) -> list[SModifiedFirmwares] | None:
    return await firmware_services.search_all_firmwares() if user else None
