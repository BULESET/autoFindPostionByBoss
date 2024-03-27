# @Time :       3.1.24 6:39 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       login.py
# @Project :    autoFindPositionByBoss
# @Description:

class LoginPage(object):
    # apply_for_job_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/ul/li[1]'
    # recruit_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/ul/li[2]'
    input_box = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/span[2]/input'
    input_box_background_content = '手机号'
    area_code = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]'
    sms_code_input_box = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/span/input'
    # sms_code_input_background_content = '短信验证码'
    sms_code_send_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/span/div'
    check_send_sms_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[3]'
    login_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/button'
    register_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/button'
    wechat_login_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/div[4]/a'
    wechat_register_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/div[4]/a'
    agreement_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[2]/span/input'
    qr_code_login_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[1]'


class ApplyForJobPage(LoginPage):
    apply_for_job_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/ul/li[1]'


class RecruitPage(LoginPage):
    recruit_button = '//*[@id="wrap"]/div/div[2]/div[2]/div[2]/div[1]/ul/li[2]'
