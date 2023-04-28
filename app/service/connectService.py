from app.entities.model_connection_info import ConnectionInfo
from app.core.db.baseAsync import session


class ConnectionInfoService:
    ### 구현함수
    ### register: 
    ### update:
    ### delete:
    ### get

    async def register(input:ConnectionInfo)-> ConnectionInfo:
        session.add(input)
        await session.commit()
        #session.refresh(input)
        return input

    def update():
        pass

    def delete():   
        pass

    def get():
        pass


    pass