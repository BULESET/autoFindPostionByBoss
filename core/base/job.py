# @Time :       1.11.23 2:26 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       job.py
# @Project :    PositionRecommend
# @Description:
from abc import ABCMeta, abstractmethod


class Job(metaclass=ABCMeta):

    @abstractmethod
    def getJobList(self, job_from):
        pass

    @abstractmethod
    def getJobDetail(self, job_from):
        pass
