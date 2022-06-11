from datetime import datetime

from fastapi import FastAPI
import aiohttp
import asyncio

HEADERS = {"User-Agent": "zhang shang zhong you/6.1.1 (iPhone; iOS 14.6; Scale/3.00)"}
API_ROOT = "https://be-prod.redrock.cqupt.edu.cn/magipoke-jwzx/"
app = FastAPI()


@app.get("/query/{stu_id}")
def root(stu_id: int):
    start = datetime.now()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [get_exam_info(stu_id), get_kebiao_info(stu_id)]
    results = loop.run_until_complete(asyncio.gather(*tasks))
    return {"data": results[1] - results[0], "time": datetime.now() - start}


# 获取考试记录的课程
async def get_exam_info(stu_id: int):
    data = {"stuNum": stu_id}
    async with aiohttp.ClientSession() as session:
        async with session.post(API_ROOT + "examSchedule", data=data) as resp:
            resp_json = await resp.json()
            result = set()
            try:
                for exam in resp_json["data"]:
                    result.add(exam["course"])
            finally:
                return result


# 获取课表并返回一组set
async def get_kebiao_info(stu_id: int):
    data = {"stu_num": stu_id}
    async with aiohttp.ClientSession() as session:
        async with session.post(API_ROOT + "kebiao", data=data) as resp:
            resp_json = await resp.json()
            result = set()
            try:
                for exam in resp_json["data"]:
                    result.add(exam["course"])
            finally:

                return result
