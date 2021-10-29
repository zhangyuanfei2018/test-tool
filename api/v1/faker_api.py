# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 10:06 上午
# @Author  : zyf
"""
faker 测试数据
"""

from fastapi import APIRouter

from common import logger
from schema.response import response_code
from schema.request.faker_api import FakerData
from service.faker_service import test_data

router = APIRouter()


@router.post("/test/data", summary="获取随机数据", name="获取随机数据", description="获取随机数据")
async def random_data(param: FakerData):
    """
    获取随机数据
    :param param:
    :return:
    """
    logger.info(f"->/test/data的入参信息为---->{param.value}")
    if param.value == "social":
        obj_info = test_data.social_data()
    elif param.value == "organization":
        obj_info = test_data.organization_data()
    else:
        obj_info = test_data.faker_data(param.value)
    return response_code.resp_200(data=obj_info)
