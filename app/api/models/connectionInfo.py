from typing import Any, Dict, Tuple
from app.api.models.base import ModelBase
from sqlmodel import Field
from sqlalchemy import Column, String, Integer, JSON
from pydantic import BaseModel
import json 


class ConnectionInfo(ModelBase, table=True):
    __tablename__ = "connection_information"

    connection_name: str = Field(
        description="연결 컴퓨팅 정보가 담겨진 정보의 이름",
        nullable=False,
        max_length=200,
        unique=True,
        sa_column=Column(String(200), nullable=False),
    )

    host: str = Field(
        description="연결 컴퓨팅 환경의 host 정보",
        nullable=False,
        max_length=200,
        sa_column=Column(String(200), nullable=False),
    )

    port: int = Field(
        description="연결 컴퓨팅 환경의 port 정보",
        nullable=False,
        sa_column=Column(Integer(), nullable=False),
    )

    user: str = Field(
        description="연결 컴퓨팅 환경의 user 정보",
        nullable=False,
        max_length=200,
        sa_column=Column(String(200), nullable=False),
    )

    password: str = Field(
        description="연결 컴퓨팅 환경의 password 정보",
        nullable=False,
        max_length=200,
        sa_column=Column(String(200), nullable=False),
    )

    header: str = Field(
        description="컴퓨팅환경과 연결 시 필요한 header 정보",
        max_length=200,
        sa_column=Column(JSON(), nullable=True),
    )

    extra: str = Field(
        description="연결 컴퓨팅 환경의 host 정보",
        max_length=200,
        sa_column=Column(JSON(), nullable=True),
    )


class RequestByConnId(BaseModel):
    connection_name : str = Field(None, description="Information you want to find through 'connection_name'")

    class Config:
        validate_assignment: bool = True


class RequestBodyConnInfo(BaseModel):
    host : str = Field(None,nullable=True, description="Host value")
    port : str = Field(None,nullable=True ,description="port value")
    user : str = Field(None,nullable=True , description="user value")
    password : str = Field(None,nullable=True , description="password value")
    header : str= Field(None,nullable=True , description="header value",sa_column=Column(JSON(), nullable=True))
    extra :str = Field(None,nullable=True , description="extra value",sa_column=Column(JSON(), nullable=True))

    
    class Config:
        validate_assignment: bool = True