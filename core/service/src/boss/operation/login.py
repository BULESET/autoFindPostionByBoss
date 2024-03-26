# @Time :       3.1.24 7:28 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       login.py
# @Project :    PositionRecommend
# @Description:
import loguru

from core.service.src.boss.pages.login import ApplyForJobPage
from common.driver import driver
from loguru import logger
import os.path

url = 'https://www.zhipin.com/web/user/?ka=header-login'
next_url = 'https://www.zhipin.com/web/geek/job-recommend'


class LoginPageOperation(object):
    current_path = os.path.dirname(os.path.abspath('.'))
    tmp_path = os.path.join(current_path, 'tmpFile')

    def __init__(self, browser):
        self.browser = browser
        self.content = browser.new_context()
        self.page = self.content.new_page()

    def _send_sms_code(self, phone_number: str):
        logger.info(f'【{phone_number}手机号开始发送短信验证码】')
        logger.info(f'【输入短信验证码】')
        self.page.fill(ApplyForJobPage.input_box, phone_number)
        logger.info(f'【输入短信验证码按钮】')
        self.page.click(ApplyForJobPage.sms_code_send_button)
        logger.info(f'【发送短信验证码二次验证】')
        self.page.click(ApplyForJobPage.check_send_sms_button)

    def _input_sms_code(self, sms_code: str):
        self.page.fill(ApplyForJobPage.sms_code_input_box, sms_code)

    # TODO 此处接收短信验证码应该是异步的，需要再处理，目前没有处理
    def login_by_phone(self, phone_number: str, sms_code: str):
        self.page.goto(url)
        self.page.click(ApplyForJobPage.apply_for_job_button)
        self.page.fill(ApplyForJobPage.input_box, phone_number)
        self._send_sms_code(phone_number)
        self.page.wait_for_timeout(1500)
        self._input_sms_code(sms_code)
        self.page.click(ApplyForJobPage.login_button)
        self.content.storage_state(path=os.path.join(self.tmp_path, 'login_data.json'))

    # TODO 此处需要接收boss直聘登录的二维码并发送到指定微信、钉钉、企业微信、飞书、邮件、或者微信工作号等平台,此处需要再处理，目前没有处理
    def login_by_qr_code(self):
        self.page.goto(url)
        self.page.click(ApplyForJobPage.qr_code_login_button)
        self.page.screenshot(path=os.path.join(self.tmp_path, 'qr_code_images', 'qr_cod.png'))
        self.page.wait_for_url(next_url)
        self.content.storage_state(path=os.path.join(self.tmp_path, 'login_data.json'))

    # TODO 此处需要接收微信登录的二维码并发送到指定微信、钉钉、企业微信、飞书、邮件、或者微信工作号等平台,此处需要再处理，目前没有处理
    def login_by_wechat(self):
        self.page.goto(url)
        self.page.click(ApplyForJobPage.agreement_button)
        self.page.click(ApplyForJobPage.wechat_login_button)
        self.page.screenshot(path=os.path.join(self.tmp_path, 'wechat_images', 'wechat_login.png'))
        self.page.wait_for_url(next_url)
        self.content.storage_state(path=os.path.join(self.tmp_path, 'login_data.json'))

    # TODO 此处需要接收微信登录的二维码并发送到指定微信、钉钉、企业微信、飞书、邮件、或者微信工作号等平台,此处需要再处理，目前没有处理
    def register_by_wechat(self):
        self.page.goto(url)
        self.page.click(ApplyForJobPage.agreement_button)
        self.page.click(ApplyForJobPage.wechat_register_button)
        self.page.wait_for_url(next_url)
        self.content.storage_state(path=os.path.join(self.tmp_path, 'login_data.json'))


if __name__ == '__main__':
    R = driver()
    L = LoginPageOperation(browser=R)
    L.login_by_qr_code()
