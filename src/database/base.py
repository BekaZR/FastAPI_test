from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.settings import settings

async_engine = create_async_engine(
    settings.database_uri,
    future=True,
    pool_size=20,
    pool_pre_ping=True,
    pool_use_lifo=True,
    echo=settings.echo,
)

async_session = sessionmaker(
    future=True,
    class_=AsyncSession,
    bind=async_engine,
    expire_on_commit=False,
)

Base = declarative_base()
