# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 1:15 下午
# @Author  : zyf

from faker import Faker

from utils.social import company_code


class TestData:
    def __init__(self):
        self.faker = Faker("zh_CN")

    def faker_data(self, data_type: str) -> str:
        """
        通过faker获取测试数据
        :param data_type:
        :return:
        """
        return getattr(self.faker, data_type)()

    @staticmethod
    def social_data() -> str:
        """
        获取社会统一信用代码
        :return:
        """
        return company_code.create_social_credit()

    @staticmethod
    def organization_data() -> str:
        """
        获取组织机构代码
        :return:
        """
        return company_code.create_organization()


test_data = TestData()
