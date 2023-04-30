import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
sys.path.append("/home/cucuridas/chatbot")
from typing import Union
from fastapi import FastAPI
from app.api.routers.connect import connect_router


"""
fastapi 서버를 실행 시키는 파일입니다
"""


def createApp() -> FastAPI:
    fastApiServer = FastAPI()
    fastApiServer.include_router(connect_router)

    return fastApiServer


app: FastAPI = createApp()
