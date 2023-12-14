# @Time :       2.11.23 10:11 上午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       url.py
# @Project :    PositionRecommend
# @Description:
from enum import Enum


class Urls(Enum):
    BOSS = 'https://www.zhipin.com'


class GetURL(object):
    """获取文件MineType"""

    @staticmethod
    def get_type(urlType):
        member = Urls.__members__.get(urlType.lower())
        return member.value


if __name__ == '__main__':
    pass
