# @Time :       3.1.24 7:28 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       login.py
# @Project :    PositionRecommend
# @Description:

from core.service.src.boss.pages.login import ApplyForJobPage
from common.driver import driver

url = 'https://www.zhipin.com/web/user/?ka=header-login'


class LoginPageOperation(object):
    page = driver()

    def _send_sms_code(self, phone_number: str):
        self.page.fill(ApplyForJobPage.input_box, phone_number)
        self.page.click(ApplyForJobPage.sms_code_send_button)
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

    # TODO 此处需要接收boss直聘登录的二维码并发送到指定微信、钉钉、企业微信、飞书、邮件、或者微信工作号等平台,此处需要再处理，目前没有处理
    def login_by_qr_code(self):
        self.page.goto(url)
        self.page.click(ApplyForJobPage.qr_code_login_button)
        self.page.wait_for_timeout(3000)
        self.page.screenshot(
            path='ss.png')

    # TODO 此处需要接收微信登录的二维码并发送到指定微信、钉钉、企业微信、飞书、邮件、或者微信工作号等平台,此处需要再处理，目前没有处理
    def login_by_wechat(self):
        self.page.goto(url)
        self.page.click(ApplyForJobPage.agreement_button)
        self.page.click(ApplyForJobPage.wechat_login_button)

    # TODO 此处需要接收微信登录的二维码并发送到指定微信、钉钉、企业微信、飞书、邮件、或者微信工作号等平台,此处需要再处理，目前没有处理
    def register_by_wechat(self):
        self.page.goto(url)
        self.page.click(ApplyForJobPage.agreement_button)
        self.page.click(ApplyForJobPage.wechat_register_button)


if __name__ == '__main__':
    L = LoginPageOperation()
    L.login_by_qr_code()
