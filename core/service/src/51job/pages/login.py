# @Time :       3.1.24 6:39 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       login.py
# @Project :    PositionRecommend
# @Description:

class LoginPage(object):
    input_box = 'tel'
    input_box_background_content = '手机号'
    area_code = 'dropdown-select'
    sms_code_input_box = 'ipt-wrap'
    sms_code_input_background_content = '短信验证码'
    sms_code_send_button = 'send_sms_code_click'
    login_button = 'sure-btn'
    register_button = 'sure-btn'
    wechat_login_button = ''
    wechat_register_button = ''
    agreement_button = ''
    qr_code_login_button = ''


class ApplyForJobPage(LoginPage):
    pass


class RecruitPage(LoginPage):
    pass


class LoginOperation(object):

    def login_by_phone(self):
        pass

    def login_by_qr_code(self):
        pass

    def login_by_wechat(self):
        pass


if __name__ == '__main__':
    print(ApplyForJobPage.input_box)
