
from fastapi import APIRouter, Request, Body, Depends, Path
from app.entities.model_connection_info import ConnectionInfo
from app.service.connectService import ConnectionInfoService
connect_router: APIRouter = APIRouter(tags=["team"]) 



@connect_router.post("/connect/register", name="connection 정보를 DB에 등록",response_model=ConnectionInfo)
async def result(request: ConnectionInfo):
    await ConnectionInfoService.register(request)

    return request