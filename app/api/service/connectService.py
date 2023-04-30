from app.api.models.connectionInfo import ConnectionInfo,RequestBodyConnInfo
from app.core.database import session
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

    async def register(self,input: ConnectionInfo) -> ConnectionInfo:
        '''

        '''
        session.add(input)
        await session.commit()
        return input

    async def update(self,input: RequestBodyConnInfo,id:int )-> ConnectionInfo:
        information = await self.get(id)

        if information:

            for key, value in input.__dict__.items():
                if value is None or key == "_sa_instance_state":
                    continue
                else :
                    setattr(information,key,value)

        else:
            raise ValueError("Error")
            

        session.add(information)
        await session.commit()
        return "Success"

    async def delete(self,id:int):
        information = await self.get(id)
        await session.delete(information)
        await session.commit()
        return "Success"

    async def get(self,id: int):
        query = select(ConnectionInfo).where(
            ConnectionInfo.id == id
        )

        information = await session.scalar(query)

        return information

    async def getByName(self,connection_name: str):
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
