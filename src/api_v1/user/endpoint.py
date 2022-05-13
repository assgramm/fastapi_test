from sqlite3 import IntegrityError
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.api_v1.user.repo import UserRepo

from src.api_v1.user.schema import UserCreate, UserView
from src.db.database import get_db_session


user_router = APIRouter()


@user_router.post('/user/create',
                  status_code=201,
                  response_model=UserView,
                  summary='Добавить нового пользователя')
async def create_user(
        user_in: UserCreate,
        db_session: AsyncSession = Depends(get_db_session),
        user_repo: UserRepo = Depends()
) -> UserView:
    try:
        user = await user_repo.add_user(db_session, user_in)
    except IntegrityError:
        raise HTTPException(
            status_code=404,
            detail="Пользователь с данным Telegram ID уже внесен в базу данных",
        )
    return user
