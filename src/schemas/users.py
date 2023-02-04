from src.schemas.base import BaseSchema


class UserCreateSchema(BaseSchema):
    name: str
    password: str


class UserGetSchema(BaseSchema):
    id: int
    name: str
    password: str