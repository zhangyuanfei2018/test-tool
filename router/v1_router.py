# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 3:55 下午
# @Author  : zyf
"""

版本路由区分

# 可以在这里添加所需要的依赖
https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi

fastapi 没有像flask那样 分组子路由没有 middleware("http") 但是有 dependencies

"""

from fastapi import APIRouter, Depends

from api.v1.sys_scheduler import router as scheduler_router
from api.v1.sys_api import router as sys_api_router
from api.v1.faker_api import router as test_data_router


api_v1_router = APIRouter()


api_v1_router.include_router(scheduler_router, tags=["任务调度"])
api_v1_router.include_router(sys_api_router, tags=["服务API管理"])
api_v1_router.include_router(test_data_router, tags=["测试数据api"])
