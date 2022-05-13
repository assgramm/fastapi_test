from typing import AsyncGenerator

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import DB, load_config


def make_connection_string(db: DB, async_fallback: bool = False) -> str:
    result = (
        f"postgresql+asyncpg://{db.user}:{db.password}@{db.host}:{db.port}/{db.name}"
    )
    if async_fallback:
        result += "?async_fallback=True"
    return result


def sa_sessionmaker(db: DB, echo: bool = False) -> sessionmaker:
    engine = create_async_engine(make_connection_string(db), echo=True)
    return sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession,
        future=True,
        autoflush=False,
    )


async def get_db_session() -> AsyncSession:
    config = load_config()
    session = sa_sessionmaker(config.db)
    async with session() as session:
        try:
            yield session
        except SQLAlchemyError as sql_ex:
            await session.rollback()
            raise sql_ex
        except HTTPException as http_ex:
            await session.rollback()
            raise http_ex
        finally:
            await session.close()
