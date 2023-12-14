# @Time :       1.11.23 2:23 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       login.py
# @Project :    PositionRecommend
# @Description:
from abc import ABCMeta, abstractmethod


class Login(metaclass=ABCMeta):

    @abstractmethod
    def loginByAccount(self, username, password):
        pass

    @abstractmethod
    def loginByPhone(self, phoneNumber, smsCode):
        pass
