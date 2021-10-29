# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 3:18 下午
# @Author  : zyf

"""

一些通用的依赖功能

"""
from typing import Generator, Any, Union, Optional


from db.session import SessionLocal


def get_db() -> Generator:
    """
    获取sqlalchemy会话对象
    :return:
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()




