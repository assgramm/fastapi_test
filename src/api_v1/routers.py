from fastapi import APIRouter

from src.api_v1.user.endpoint import user_router

api_router = APIRouter()

api_router.include_router(user_router, tags=["Пользователь"])
