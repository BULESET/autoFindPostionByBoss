# @Time :       3.1.24 4:57 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       chat.py
# @Project :    PositionRecommend
# @Description:


from abc import ABCMeta, abstractmethod


class Chat(metaclass=ABCMeta):

    @abstractmethod
    def chat(self, platform_type, content: str):
        pass
