# @Time :       3.1.24 9:37 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       index.py
# @Project :    PositionRecommend
# @Description:
from core.service.src.boss.pages.index import IndexPage
from common.driver import driver

url = 'https://www.zhipin.com/beijing/'


class IndexPageOperation(object):
    page = driver()

    def search(self, search_content: str):
        self.page.goto(url)
        self.page.fill(IndexPage.search_box, search_content)
        self.page.click(IndexPage.search_button)
