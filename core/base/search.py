# @Time :       3.1.24 4:52 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       search.py
# @Project :    PositionRecommend
# @Description:


from abc import ABCMeta, abstractmethod


class Search(metaclass=ABCMeta):

    @abstractmethod
    def searchPosition(self, platform_type, position: str, search_condition: object):
        pass

    @abstractmethod
    def searchCompany(self, platform_type, company: str, search_condition: object):
        pass
