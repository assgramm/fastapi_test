from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    first_name: str = Field(..., title='Имя пользователя')
    last_name: str = Field(..., title='Фамилия пользователя')

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    phone_number: Optional[str] = Field(None, title='Номер телефона')
    email: Optional[str] = Field(None, title='Email пользователя')
    username: str = Field(..., title='Username пользователя')


class UserView(UserBase):
    id: int = Field(..., title='ID пользователя')
    phone_number: Optional[str] = Field(None, title='Номер телефона')
    email: Optional[str] = Field(None, title='Email пользователя')
    username: str = Field(..., title='Username пользователя')
    created_at: datetime = Field(..., title='Дата регистрация')
    updated_at: datetime = Field(..., title='Дата изменения')

    class Config:
        json_encoders = {
            datetime: lambda v: datetime.strftime(v, "%d.%m.%Y %H:%M")
        }
