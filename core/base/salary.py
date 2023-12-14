# @Time :       1.11.23 2:31 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       salary.py
# @Project :    PositionRecommend
# @Description:

from abc import ABCMeta, abstractmethod


class Salary(metaclass=ABCMeta):

    @abstractmethod
    def getSalary(self, login_from):
        pass

    @abstractmethod
    def salaryRanking(self):
        pass
