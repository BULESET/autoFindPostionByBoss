# @Time :       4.1.24 2:46 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       search.py
# @Project :    autoFindPositionByBoss
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
    current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tmp_path = os.path.join(current_path, 'tmpFile', 'login_data.json')
    js = "const js = `Object.defineProperty(navigator, 'webdriver', {get: () => undefined})`;"

    def __init__(self, browser, chatWithHRAgain=False, content=None, page=None):
        """

        :param browser: 浏览器实例
        :param chatWithHRAgain: 是否和已经聊过的继续聊,否的话是不在继续和已经聊过的hr聊天，是的话继续和已经聊过天的HR聊天
        :param content: 上下文实例
        :param page: page实例
        """

        if not checkoutLoginFile():
            self.login_instance = LoginPageOperation(browser)
            self.login_instance.login_by_qr_code()
            self.browser = browser
            self.content = self.login_instance.content
            self.page = self.login_instance.page
            self.page.evaluate(self.js)
            self.goToSearchPage()

        else:
            if not browser.contexts:
                self.browser = browser
                self.content = browser.new_context(storage_state=self.tmp_path, no_viewport=True)
                self.page = self.content.new_page()
                self.page.evaluate(self.js)
                self.goToSearchPage()
            else:
                self.browser = browser
                self.content = content
                self.page = page
                self.page.evaluate(self.js)

        self.chatWithHRAgain = chatWithHRAgain
        self.send_message_status = None

    def goToSearchPage(self):
        self.page.goto(url=self.url)
        self.page.wait_for_url(self.url)

    def searchJob(self, job_name: [list, str], **kwargs):
        logger.info('【开始输入岗位名称】')
        self.page.fill(Search().search_job.search_box, job_name)
        logger.info('【开始搜索岗位】')
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
                    self.send_message_status = JobDetailPageOperation(self.browser, self.content,
                                                                      job_detail_page).chatWithHRAtNow(
                        chatWithHRAgain=self.chatWithHRAgain)

            logger.info('【已经遍历完在线数据】')
            return True
        else:
            logger.info('【当前页面没有HR在线】')
            return True

    def goToNextSearchPage(self):
        current_url = copy.deepcopy(self.page.url)
        if self.page.locator(Search().search_job.next_page_button).is_visible():
            logger.info('【下一页按钮可见】')
            logger.info('【点击下一页】')
            self.page.locator(Search().search_job.next_page_button).click()
            logger.info('【下一页按钮点击完成】')
            logger.info(f'【当前页面URL】:{self.page.url}')
            if current_url == self.page.url:
                logger.info('【已经到头啦】')
                return False
            return True

        else:
            logger.info('【下一页按钮不可见】')
            return False

    def goFirstSearchPage(self):
        logger.info('【点击第一页】')
        self.page.locator(Search().search_job.first_page_button).click()

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

    def start(self, job_name: [list, str], **kwargs):
        logger.info(f'【入参职位名称为:{job_name}】')
        if isinstance(job_name, str):
            logger.info(f'【需要搜索的职位名称为:{job_name}】')
            time.sleep(3)
            self.searchJob(job_name)
            time.sleep(4)
            while self.chatWithOnLineHR():
                time.sleep(4)
                if self.send_message_status == 'unable_chat_today':
                    break
                if not self.goToNextSearchPage():
                    time.sleep(3)
                    break

        if isinstance(job_name, list) and len(job_name) == 1:
            logger.info(f'【需要搜索的职位名称为:{job_name}】')
            time.sleep(3)
            self.searchJob(job_name[0])
            time.sleep(4)
            while self.chatWithOnLineHR():
                time.sleep(4)
                if self.send_message_status == 'unable_chat_today':
                    break
                if not self.goToNextSearchPage():
                    time.sleep(3)
                    break

        #
        if isinstance(job_name, list):
            for job in job_name:
                logger.info(f'【需要搜索的职位名称为:{job}】')
                time.sleep(4)
                self.searchJob(job)
                time.sleep(4)
                while self.chatWithOnLineHR():
                    time.sleep(4)
                    if not self.goToNextSearchPage():
                        time.sleep(4)
                        break
                if self.send_message_status == 'unable_chat_today':
                    break
        self.start(job_name)

    def close(self):
        self.content.close()
        self.page.close()


if __name__ == '__main__':
    pass
    R = driver()
    S = SearchJobPageOperation(R)
    S.start(job_name=['移动端测试工程师', '软件测试工程师', '自动化测试工程师'])
    time.sleep(3)
