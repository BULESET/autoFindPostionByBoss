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
    js = "Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});"

    def __init__(self, browser, content=None, page=None):

        if not checkoutLoginFile():
            self.login_instance = LoginPageOperation(browser)
            self.content = self.login_instance.content
            self.login_instance.login_by_qr_code()
            self.page = self.content.new_page()
            self.page.add_init_script(self.js)
            self.browser = browser

        else:
            if not browser.contexts:
                self.browser = browser
                self.content = browser.new_context(storage_state=self.tmp_path, no_viewport=True)
                self.page = self.content.new_page()
                self.page.add_init_script(self.js)

            else:
                self.browser = browser
                self.content = content
                self.page = page
                self.page.add_init_script(self.js)

    def gotoJobDetailPage(self, url):
        self.page.goto(url)

    def chatWithHRAtNow(self, NotChatWithCompanyList: [None, list] = None, chatWithHRAgain=True):
        if isinstance(NotChatWithCompanyList, (str, list)):
            if self.getCompanyName() in NotChatWithCompanyList:
                self.page.close()

        if not chatWithHRAgain and '继续沟通' == self.checkButtonText():
            self.pageClosed()

        else:
            self.page.click(DetailPage().communication_button)
            send_status = ChatWithHROperation(self.browser, self.content, self.page).send_message()
            ChatWithHROperation(self.browser, self.content, self.page).close(closePopupPage=True)
            return send_status

    def getJobInfo(self):
        pass

    def checkButtonText(self):
        return self.page.locator(DetailPage().communication_button).inner_text()

    def chatWithHRAgain(self):
        self.page.click(DetailPage().communication_button_again)

    def getJobDescribeContent(self):
        return self.page.locator(DetailPage().job_describe_content).inner_text()

    def getHrName(self):
        return self.page.locator(DetailPage().hr_name).inner_text()

    def getJobName(self):
        return self.page.locator(DetailPage().job_name).inner_text()

    def getHrActiveTime(self):
        return self.page.locator(DetailPage().hr_active_time).inner_text()

    def getCompanyName(self):
        return self.page.locator(DetailPage().business_information_company_name).inner_text()

    def getJobMoney(self):
        money = self.page.locator(DetailPage().job_money).inner_text().split('-')
        min_money = money[0] + 'K'
        max_money = money[1]
        if '·' in max_money:
            max_money = self.page.locator(DetailPage().job_money).inner_text().split('-')[1].split('·')[0]
            return min_money, max_money
        else:
            return min_money, max_money

    def getCompanyLocationAddress(self):
        return self.page.locator(DetailPage().company_location_address).inner_text()

    def pageClosed(self):
        self.page.close()

    def getPageTitle(self):
        return self.page.title()


if __name__ == '__main__':
    R = driver()
    url = 'https://www.zhipin.com/job_detail/8de1ae0ce596f2151nJ72t28EFJQ.html?lid=1ZbJC6KeFUa.search.59&securityId=c99ifTJJs6msM-G1zst4Q7ncx42T6hSfSP_v37NwZhUIcnf5AuuKsRIYXTHfcrl48h2gUbn9Ak1JDdR5lUL2tMw1Z1ZPL3cffSm1er35UReUIMH8&sessionId='

    J = JobDetailPageOperation(R)
    J.gotoJobDetailPage(url=url)
    print(J.getJobMoney())
    print(J.getJobDescribeContent())
    print(J.getJobName())
