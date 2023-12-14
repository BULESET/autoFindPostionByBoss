# @Time :       1.11.23 2:27 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       sms.py
# @Project :    PositionRecommend
# @Description:

from abc import ABCMeta, abstractmethod


class SMS(metaclass=ABCMeta):

    @abstractmethod
    def getSMS(self, login_from):
        pass


