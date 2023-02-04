from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from src.database.base import Base



class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = Column(Integer, primary_key=True, index=True, unique=True)
    name: Mapped[str] = Column(String(30), nullable=False)
    password: Mapped[str] = Column(String(1000), nullable=False)