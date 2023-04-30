from fastapi import APIRouter, Request, Body, Depends, Path
from app.api.models.model_connection_info import ConnectionInfo
from app.api.service.connectService import ConnectionInfoService
from typing import List

connect_router: APIRouter = APIRouter(tags=["team"])


@connect_router.post(
    "/connect/register", name="connection 정보를 DB에 등록", response_model=ConnectionInfo
)
async def result(request: ConnectionInfo):
    await ConnectionInfoService(request).register()

    return request


@connect_router.put(
    "/connect/update", name="등록된 conenction 정보를 수정", response_model=ConnectionInfo
)
async def result(request: ConnectionInfo):
    await ConnectionInfoService(request).update()

    return request


@connect_router.delete(
    "/connect/delete", name="등록된 conenction 정보를 삭제", response_model=ConnectionInfo
)
async def result(request: ConnectionInfo):
    await ConnectionInfoService(request).delete()

    return request


@connect_router.get(
    "/connect/get", name="등록된 conenction 단일 정보를 조회", response_model=ConnectionInfo
)
async def result(request: ConnectionInfo):
    await ConnectionInfoService(request).get()
    return request


@connect_router.get(
    "/connect/gets",
    name="등록된 conenction 모든 정보를 조회",
    response_model=List[ConnectionInfo],
)
async def result(request: ConnectionInfo):
    await ConnectionInfoService(request).gets()

    return request
