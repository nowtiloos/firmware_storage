from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.dependencies.services import get_users_services
from app.models.users import Users
from app.schemas.users import SUsers
from app.services.users import UsersServices

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.get("/me")
def read_users_me(user: Users = Depends(get_current_user),
                  users_services: UsersServices = Depends(get_users_services)) -> SUsers:
    return users_services.read_users_me(user)