from asyncio import current_task

from sqlmodel import SQLModel
from app.core.config import Settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import (
    async_scoped_session,
    create_async_engine,
    AsyncEngine,
)
from sqlalchemy.ext.asyncio.session import AsyncSession
from typing import Union


"""
sqlAlchemy를 통해 orm 사용하기위해 정의되는 python 파일입니다 engine을 통해 연결 객체를 입력받아
sessionmaker 클래스를 통해 session 연결을 진행합니다

"""

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{Settings.DB_USER}:{Settings.DB_PASS}@{Settings.DB_HOST}:{Settings.DB_PORT}/{Settings.DB_NAME}"

engine: AsyncEngine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True)
session_maker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

session: Union[AsyncSession, async_scoped_session] = async_scoped_session(
    session_factory=session_maker,
    scopefunc=current_task,
)


metadata = SQLModel.metadata
#metadata.naming_convention = NAMING_CONVENTION
Base = declarative_base(metadata=metadata)