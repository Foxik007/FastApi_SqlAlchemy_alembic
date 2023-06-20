from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:7259512aA@localhost:5432/postgres"


metadata = MetaData()

engine = create_async_engine(DATABASE_URL,future=True,echo=True)
async_session_maker = sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

