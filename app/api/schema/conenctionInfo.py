from pydantic import BaseModel, Field, Json
from typing import Optional, Any


class ReqConnectionInfo(BaseModel):
    connection_name: str = Field(
        title="connection 정보 이름", description="connection 정보를 찾기위한 이름"
    )
    host: str = Field(title="Connection Host 정보", description="Connection 호스트 정보")
    port: int = Field(title="Connection Port 정보", description="Port 정보")
    user: str = Field(title="Connection User 정보", description="User 정보")
    password: str = Field(title="Connection password 정보", description="password 정보")
    header: Optional[Json[Any]] = Field(
        title="Connection header 정보", description="header 정보"
    )
    extra: Optional[Json[Any]] = Field(title="Connection 추가 정보", description="추가 정보")

    class Config:
        schema_extra = {
            "example": {
                "connection_name": "test_conn1",
                "host": "localhost",
                "port": 1233,
                "user": "ubuntu",
                "password": "test123",
            }
        }
