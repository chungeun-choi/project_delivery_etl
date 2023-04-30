import sys

sys.path.append("/Users/cucuridas/Desktop/project_delivery_etl")
import asyncio
from app.service.connectService import *


# class function - register 함수 테스트
async def test_register(input: ConnectionInfo):
    value = await ConnectionInfoService(input).register()

    print(value)


# class function - update 함수 테스트
async def test_update(input: ConnectionInfo):
    value = await ConnectionInfoService(input).update()

    print(value)


# class function - get 함수 테스트
async def test_get(input: ConnectionInfo):
    value = await ConnectionInfoService(input).get()
    print(value)


# class function = delete 함수 테스트
async def test_delete(input: ConnectionInfo):
    value = await ConnectionInfoService(input).delete()
    print(value)


if __name__ == "__main__":
    ## True value
    true_value = {
        "input": ConnectionInfo(
            connection_name="test_obj_0430",
            host="192.168.1.2",
            port=9300,
            user="elastic",
            password="test21!",
        )
    }

    ## register
    # asyncio.run(test_register(**true_value))

    ## get
    # asyncio.run(test_get(ConnectionInfo(connection_name="Ther is no")))

    # update
    asyncio.run(test_update(**true_value))

    # delete
    # asyncio.run(test_delete(ConnectionInfo(connection_name="Ther is no")))

    # ## False value
    # false_value1 = {
    #     "input":ConnectionInfo(
    #     connection_name="test_conenction",
    #     host="test@101.1.1.1",
    #     port=8080,
    #     user="testuser",
    #     password="test11!",
    # )
    # }

    # asyncio.run(test_check_info(**true_value))

    # asyncio.run(test_check_info(**false_value))
