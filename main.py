import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.routers import api_router
from src.db.database import get_db_session


def main() -> FastAPI:
    fastapi = FastAPI()

    fastapi.include_router(api_router)

    fastapi.dependency_overrides[AsyncSession] = get_db_session

    return fastapi


app = main()

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True, log_config='logs/logger.yml')
