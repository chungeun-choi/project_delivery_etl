from fastapi import APIRouter, Request, Body, Depends, Path
from app.api.models.connectionInfo import ConnectionInfo,RequestBodyConnInfo
from app.api.service.connectService import ConnectionInfoService
from typing import List

connect_router: APIRouter = APIRouter(tags=["connection_info"])
con_info_obj = ConnectionInfoService()

@connect_router.post(
    "/connect/register", name="connection 정보를 DB에 등록", response_model=ConnectionInfo
)
async def register(request: ConnectionInfo):
    await con_info_obj.register(request)

    return request


@connect_router.put(
    "/connect/{connection_id}/update", name="등록된 conenction 정보를 수정", response_model=str
)
async def update(request: RequestBodyConnInfo,connection_id:int = Path(description="Conenction id")):
    return_value = await con_info_obj.update(request,connection_id)

    return return_value


@connect_router.delete(
    "/connect/{connection_id}/delete", name="등록된 conenction 정보를 삭제", response_model=str
)
async def delete(connection_id: int = Path(description="Connection id")):
    return_value = await con_info_obj.delete(connection_id)

    return return_value


@connect_router.get(
    "/connect/{connection_name}/get", name="등록된 conenction 단일 정보를 조회", response_model=ConnectionInfo
)
async def get(connection_name: str = Path(description="Connection name")):
    return_value = await con_info_obj.getByName(connection_name)
    return return_value


@connect_router.get(
    "/connect/gets",
    name="등록된 conenction 모든 정보를 조회",
    response_model=List[ConnectionInfo],
)
async def gets():
    return_value = await con_info_obj.gets()

    return return_value
