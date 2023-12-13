from app.interfaces.repository import IUsersRepository
from app.models.users import Users
from app.repositories.base_repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository, IUsersRepository):
    model = Users
