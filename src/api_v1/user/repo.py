from typing import Optional, List

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.user.model import User
from src.api_v1.user.schema import UserCreate


class UserRepo:
    model = User

    async def add_user(self, db_session: AsyncSession, obj_in: UserCreate) -> Optional[model]:
        sql = insert(self.model).values(**obj_in.dict()).returning('*')
        result = await db_session.execute(sql)
        return result.first()

    async def get_id(self, db_session: AsyncSession, model_id: int) -> Optional[model]:
        sql = select(self.model).where(self.model.id == model_id)
        request = await db_session.execute(sql)
        result = request.scalar()
        return result

    async def get_all(self, db_session: AsyncSession, skip: int = 0, limit: int = 100) -> List[model]:
        sql = select(self.model).offset(skip).limit(limit)
        request = await db_session.execute(sql)
        result = request.scalars().all()
        return result
