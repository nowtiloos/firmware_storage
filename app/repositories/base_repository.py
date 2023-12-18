from sqlalchemy import select, insert, delete, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession

from app.interfaces.repository import IRepository


class SQLAlchemyRepository(IRepository):
    model = None

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def find_all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def find_by_filter(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def find_one_or_none(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(stmt)
        return result.scalars().one_or_none()

    async def add(self, **data) -> bool:
        stmt = insert(self.model).values(**data)
        await self.session.execute(stmt)
        return True

    async def delete(self, **filter_by) -> None:
        stmt = delete(self.model).filter_by(**filter_by)
        await self.session.execute(stmt)
