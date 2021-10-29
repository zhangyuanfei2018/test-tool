# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 2:53 下午
# @Author  : zyf
"""
test: 测试环境
prod: 生产环境
部署时请务必更新为生产环境
"""

env = "test"

if env == "prod":
    # 如果有虚拟环境 则是 生产环境
    print("----------生产环境启动------------")
    from .prod_config import settings
elif not env or env == "test":
    # 没有则是开发环境
    print("----------开发环境启动------------")
    from .test_config import settings
