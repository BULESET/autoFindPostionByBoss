# @Time :       1.11.23 2:29 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       company.py
# @Project :    PositionRecommend
# @Description:
from abc import ABCMeta, abstractmethod


class Company(metaclass=ABCMeta):

    @abstractmethod
    def getCompany(self, login_from):
        pass


