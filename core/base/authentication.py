# @Time :       1.11.23 2:35 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       authentication.py
# @Project :    PositionRecommend
# @Description:

from abc import ABCMeta, abstractmethod


class Authentication(metaclass=ABCMeta):

    @abstractmethod
    def getToken(self, login_type):
        pass

    @abstractmethod
    def cookie(self):
        pass
