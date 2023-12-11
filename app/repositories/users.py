from abc import ABC

from app.models.users import Users
from app.utils.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository, ABC):
    model = Users
