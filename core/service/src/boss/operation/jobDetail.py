# @Time :       25.3.24 2:01 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       jobDetail.py
# @Project :    autoFindPositionByBoss
# @Description:
import time

from core.service.src.boss.operation.login import LoginPageOperation
from core.service.src.boss.pages.jobDetail import DetailPage
from core.service.src.boss.operation.chat import ChatWithHROperation

from common.driver import driver
import os.path

from core.service.src.boss.utils.tools import checkoutLoginFile


class JobDetailPageOperation(object):
    current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tmp_path = os.path.join(current_path, 'tmpFile', 'login_data.json')

    def __init__(self, browser, content=None, page=None):

        if not checkoutLoginFile():
            self.login_instance = LoginPageOperation(browser)
            self.content = self.login_instance.content
            self.login_instance.login_by_qr_code()
            self.page = self.content.new_page()
            self.browser = browser

        else:
            if not browser.contexts:
                self.browser = browser
                self.content = browser.new_context(storage_state=self.tmp_path)
                self.page = self.content.new_page()

            else:
                self.browser = browser
                self.content = content
                self.page = page

    def gotoJobDetailPage(self, url):
        self.page.goto(url)

    def chatWithHRAtNow(self, chatWithHRAgain=True):

        if not chatWithHRAgain and '继续沟通' == self.checkButtonText():
            self.pageClosed()

        else:
            self.page.click(DetailPage().communication_button)
            ChatWithHROperation(self.browser, self.content, self.page).send_message()
            ChatWithHROperation(self.browser, self.content, self.page).close(closePopupPage=True)

    def checkButtonText(self):
        return self.page.locator(DetailPage().communication_button).inner_text()

    def chatWithHRAgain(self):
        self.page.click(DetailPage().communication_button_again)

    def getJobDescribeContent(self):
        return self.page.locator(DetailPage().job_describe_content).inner_text()

    def getHrName(self):
        return self.page.locator(DetailPage().hr_name).inner_text()

    def getJobName(self):
        return self.page.locator(DetailPage().hr_name).hr_position().inner_text()

    def getHrActiveTime(self):
        return self.page.locator(DetailPage().hr_name).hr_active_time().inner_text()

    def getCompanyInfo(self):
        return self.page.locator(DetailPage().hr_name).business_information_company_name().inner_text()

    def getCompanyLocationAddress(self):
        return self.page.locator(DetailPage().hr_name).company_location_address().inner_text()

    def pageClosed(self):
        self.page.close()

    def getPageTitle(self):
        return self.page.title()


if __name__ == '__main__':
    R = driver()
    url = 'https://www.zhipin.com/job_detail/3efca81a272f420c1nxy3tu9EFpW.html?lid=WORfSsIyAJ.search.32&securityId=DvLw4a_MNZBFL-J1eL5hAfBFZ8sIGx9mYY1CaRpr18a0i0DfQ54MBV03BCY-IAqvGXWMifI-ZHsoL1_T-bikINPv1VNT65sCNBzWd5lHRiwlXfe5Smkn&sessionId='

    J = JobDetailPageOperation(R)
    J.gotoJobDetailPage(url=url)
    print(J.getJobDescribeContent())
