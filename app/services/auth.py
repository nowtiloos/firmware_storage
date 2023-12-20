from datetime import datetime, timedelta

from fastapi import Response
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import settings
from app.interfaces.unit_of_work import IUnitOfWork

from app.exceptions.exceptions import (
    CannotAddDataToDatabase,
    IncorrectEmailOrPasswordException,
    UserAlreadyExistsException,
)
from app.schemas.auth import SUserRegister, SUserLogin

pwd_context = CryptContext(schemes="bcrypt", deprecated="auto")


class AuthServices:
    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work

    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=60)
        to_encode.update({'exp': expire})
        encoded_jwt = jwt.encode(claims=to_encode, key=settings.JWT_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt

    async def authenticate_user(self, email: EmailStr, password: str):
        async with self.unit_of_work as uow:
            user = await uow.users_repository.find_one_or_none(email=email)
            if not (user and self.verify_password(password, user.hashed_password)):
                raise IncorrectEmailOrPasswordException
            return user

    async def register_user(self, user_data: SUserRegister):
        async with self.unit_of_work as uow:
            existing_user = await uow.users_repository.find_one_or_none(email=user_data.email)
            if existing_user:
                raise UserAlreadyExistsException
            hashed_password = self.get_password_hash(user_data.password)
            new_user = await uow.users_repository.add(name=user_data.name,
                                                      email=user_data.email,
                                                      hashed_password=hashed_password,
                                                      access_to_read=False,
                                                      access_to_write=False,
                                                      tg_id=user_data.tg_id
                                                      )
            if not new_user:
                raise CannotAddDataToDatabase
            return {"message": "Регистрация успешно завершена"}

    async def login_user(self, response: Response, user_data: SUserLogin):
        user = await self.authenticate_user(user_data.email, user_data.password)
        access_token = self.create_access_token({"sub": user.name})
        response.set_cookie("fw_storage_access_token", access_token, httponly=True)
        return {"message": "Успешный вход в систему", "access_token": access_token}

    @staticmethod
    async def logout_user(response: Response):
        response.delete_cookie("fw_storage_access_token")
        return {"message": "Успешный выход из системы"}
