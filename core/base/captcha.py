# @Time :       1.11.23 2:02 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       captcha.py
# @Project :    PositionRecommend
# @Description:

from abc import ABCMeta, abstractmethod


class Captcha(metaclass=ABCMeta):

    @abstractmethod
    def getCaptcha(self, login_from):
        pass
