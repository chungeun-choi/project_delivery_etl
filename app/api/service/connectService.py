from app.api.models.connectionInfo import ConnectionInfo
from app.core.db.database import session
from app.core.db.transactional import Transactional
from app.core.db.convert import ConvertSchemaToModel
from app.api.schema.conenctionInfo import ReqConnectionInfo
from sqlmodel import select
from typing import Any


class ConnectionInfoService:
    ### 구현함수
    ### register:
    ### update:
    ### delete:
    ### get
    def __init__(self) -> None:
        pass

    @Transactional(refresh=True)
    async def register(self, input: ReqConnectionInfo, **kwargs) -> ConnectionInfo:
        """ """
        convert_value = ConvertSchemaToModel(
            model_class=ConnectionInfo, schema_class=input
        )()
        session.add(convert_value)
        return convert_value

    @Transactional(refresh=True)
    async def update(self, input: ReqConnectionInfo, id: int) -> ConnectionInfo:
        information = await self.get(id)

        if information:
            convert_value = ConvertSchemaToModel(
                model_class=information, schema_class=input
            )()

        else:
            raise ValueError("Error")

        session.add(convert_value)

        return convert_value

    async def delete(self, id: int):
        information = await self.get(id)
        await session.delete(information)
        await session.commit()
        return "Success"

    async def get(self, id: int):
        query = select(ConnectionInfo).where(ConnectionInfo.id == id)

        information = await session.scalar(query)

        return information

    async def getByName(self, connection_name: str):
        query = select(ConnectionInfo).where(
            ConnectionInfo.connection_name == connection_name
        )

        information = await session.scalar(query)

        return information

    async def gets(self):
        query = select(ConnectionInfo)

        information = await session.scalars(query)

        return information.all()

    # async def cehckBy(self, connection_name: ConnectionInfo.connection_name):
    #     query = select(ConnectionInfo).where(
    #         ConnectionInfo.connection_name == connection_name
    #     )
    #     result = await session.scalar(query)

    #     if result.first() is None:
    #         return True
    #     else:
    #         return False
