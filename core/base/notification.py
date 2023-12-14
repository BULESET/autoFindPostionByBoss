# @Time :       1.11.23 2:33 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       notification.py
# @Project :    PositionRecommend
# @Description:

from abc import ABCMeta, abstractmethod


class Notification(metaclass=ABCMeta):

    @abstractmethod
    def sendNotification(self, login_from):
        pass
