from app.api.models.model_connection_info import ConnectionInfo
from app.core.database import session
from sqlmodel import select
from typing import Any


class ConnectionInfoService:
    ### 구현함수
    ### register:
    ### update:
    ### delete:
    ### get

    def __init__(self, model_obj: ConnectionInfo):
        self.connection_model = model_obj

    async def register(self) -> ConnectionInfo:
        session.add(self.connection_model)
        await session.commit()
        return input

    async def update(self) -> ConnectionInfo:
        information = await self.get()

        information.header = self.connection_model.header
        information.extra = self.connection_model.extra
        information.host = self.connection_model.host
        information.port = self.connection_model.port
        information.user = self.connection_model.user
        information.password = self.connection_model.password

        session.add(information)
        await session.commit()

    async def delete(self):
        information = await self.get()
        await session.delete(information)
        await session.commit()
        return "Success"

    async def get(self):
        query = select(ConnectionInfo).where(
            ConnectionInfo.connection_name == self.connection_model.connection_name
        )

        information = await session.scalar(query)

        return information

    async def gets(self):
        query = select(ConnectionInfo).where(
            ConnectionInfo.connection_name == self.connection_model.connection_name
        )

        information = await session.scalars().all()

        return information

    async def _check_info(self, connection_name: ConnectionInfo.connection_name):
        query = select(ConnectionInfo).where(
            ConnectionInfo.connection_name == connection_name
        )
        result = await session.scalar(query)

        if result.first() is None:
            return True
        else:
            return False
