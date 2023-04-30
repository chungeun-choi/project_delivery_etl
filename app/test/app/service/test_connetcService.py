import sys

sys.path.append("/Users/cucuridas/Desktop/project_delivery_etl")
import asyncio
from app.api.service.connectService import *

test_obj = ConnectionInfoService()


# class function - register 함수 테스트
async def test_register(input: ConnectionInfo):
    value = await test_obj.register(input)

    print(value)


# class function - update 함수 테스트
async def test_update(input: ConnectionInfo):
    value = await test_obj.update(input)

    print(value)


# class function - get 함수 테스트
async def test_get(connetion_name: str):
    value = await test_obj.get(connetion_name)
    print(value)


# class function - gets 함수 테스트
async def test_gets():
    value = await test_obj.gets()
    print(value)


# class function = delete 함수 테스트
async def test_delete(connetion_name: str):
    value = await test_obj.delete(connetion_name)
    print(value)


if __name__ == "__main__":
    ## True value
    true_value = {
        "input": ConnectionInfo(
            connection_name="test_obj_0430",
            host="192.243.1.2",
            port=9200,
            user="telele",
            password="123123!",
        )
    }

    ## register
    #asyncio.run(test_register(**true_value))

    ## get
    #asyncio.run(test_get("test_obj_0430"))

    # gets
    #asyncio.run(test_gets())


    # update
    asyncio.run(test_update(**true_value))

    # delete
    #asyncio.run(test_delete("test_obj_0430_2"))


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
