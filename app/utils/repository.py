from abc import ABC, abstractmethod
from typing import Sequence, NoReturn

from sqlalchemy import delete, insert, select, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> NoReturn:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository, ABC):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_all(self) -> Sequence[RowMapping]:
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return result.mappings().all()

    async def find_one_or_none(self, **filter_by) -> RowMapping:
        stmt = select(self.model.__table__.columns).filter_by(**filter_by)
        result = await self.session.execute(stmt)
        return result.mappings().one_or_none()

    async def add(self, data: dict) -> None:
        stmt = insert(self.model).values(**data)
        await self.session.execute(stmt)

    async def delete(self, **filter_by) -> None:
        stmt = delete(self.model).filter_by(**filter_by)
        await self.session.execute(stmt)
