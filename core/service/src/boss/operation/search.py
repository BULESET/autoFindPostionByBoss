# @Time :       4.1.24 2:46 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       search.py
# @Project :    PositionRecommend
# @Description:
import time

from core.service.src.boss.pages.search import Search
from common.driver import driver
from core.service.src.boss.utils.tools import checkoutLoginFile
from core.service.src.boss.operation.login import LoginPageOperation
from core.service.src.boss.operation.jobDetail import JobDetailPageOperation
from loguru import logger
import copy

import os


class SearchJobPageOperation(object):
    url = 'https://www.zhipin.com/web/geek/job'
    current_path = os.path.dirname(os.path.abspath('.'))
    tmp_path = os.path.join(current_path, 'tmpFile', 'login_data.json')

    def __init__(self, browser, content=None, page=None):
        if not checkoutLoginFile():
            self.login_instance = LoginPageOperation(browser)
            self.login_instance.login_by_qr_code()
            self.browser = browser
            self.content = self.login_instance.content
            self.page = self.login_instance.page
            self.goToSearchPage()

        else:
            if not browser.contexts:
                self.browser = browser
                self.content = browser.new_context(storage_state=self.tmp_path)
                self.page = self.content.new_page()
                self.goToSearchPage()
            else:
                self.browser = browser
                self.content = content
                self.page = page

    def goToSearchPage(self):
        self.page.goto(url=self.url)
        self.page.wait_for_url(self.url)

    def searchJob(self, job_name):
        self.page.fill(Search().search_job.search_box, job_name)
        self.page.click(Search().search_job.search_button)

    def chatWithOnLineHR(self):
        logger.info('【开始遍历完在线数据】')
        hr_online_result_list = self.page.query_selector_all(Search().search_job.hr_online)
        if hr_online_result_list:
            for on_line_hr in hr_online_result_list:
                with self.content.expect_page() as new_page_info:
                    on_line_hr.click()
                    job_detail_page = new_page_info.value
                    job_detail_page.wait_for_load_state()
                    JobDetailPageOperation(self.browser, self.content, job_detail_page).chatWithHRAtNow(
                        chatWithHRAgain=False)
                time.sleep(3)
                break
            logger.info('【已经遍历完在线数据】')
            return True
        else:
            logger.info('【已经遍历完在线数据】')
            return True

    def goToNextSearchPage(self):
        current_url = copy.deepcopy(self.page.url)
        logger.info('【点击下一页】')
        if self.page.locator(Search().search_job.next_page_button).is_visible():
            logger.info('【下一页按钮可见】')
            logger.info('【点击下一页】')
            self.page.locator(Search().search_job.next_page_button).click()
            logger.info(f'【当前页面UR】L:{self.page.url}')
            logger.info('【点击完成】')
            if current_url == self.page.url:
                logger.info('【已经到头啦】')
                return False
            return True

        else:
            logger.info('【下一页不可见】')
            return False

    def goToPreviousSearchPage(self):
        current_url = copy.deepcopy(self.page.url)
        logger.info('【点击上一页】')
        if self.page.locator(Search().search_job.previous_page_button).is_visible():
            logger.info('【上一页按钮可见】')
            logger.info('【点击上一页】')
            self.page.locator(Search().search_job.previous_page_button).click()
            logger.info(f'【当前页面UR】L:{self.page.url}')
            logger.info('【点击完成】')
            if current_url == self.page.url:
                logger.info('【已经到头啦】')
                return False
            return True
        else:
            logger.info('【上一页不可见】')
            return False

    def start(self):
        while self.chatWithOnLineHR():
            if not self.goToNextSearchPage():
                break
            time.sleep(2)

    def close(self):
        self.content.close()
        self.page.close()


if __name__ == '__main__':
    R = driver()
    S = SearchJobPageOperation(R)
    time.sleep(3)
    S.searchJob('软件测试工程师')
    time.sleep(3)
    S.start()
    time.sleep(3)
