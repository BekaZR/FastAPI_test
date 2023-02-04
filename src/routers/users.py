from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.schemas.users import UserCreateSchema
from src.database.dependencies import get_async_session
from src.database.models.users import User

router = APIRouter()


@router.post("/user")
async def create_user(user: UserCreateSchema, session: AsyncSession = Depends(get_async_session)):
    user_db = User(**user.dict())
    session.add(user_db)
    await session.commit()
    return user_db


@router.get("/users/")
async def get_user_list(session: AsyncSession = Depends(get_async_session)):
    return (await session.scalars(select(User))).all()
