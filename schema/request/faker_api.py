# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 10:09 上午
# @Author  : zyf
from enum import Enum

from fastapi import FastAPI


class FakerData(str, Enum):
    name = "name"
    address = "address"
    text = "text"
    company = "company"
    user_agent = "user_agent"
    credit_card_full = "credit_card_full"
    free_email = "free_email"
    ssn = "ssn"
    social = "social"
    organization = "organization"
    phone_number = "phone_number"
