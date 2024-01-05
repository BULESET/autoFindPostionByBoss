# @Time :       3.1.24 9:47 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       jobDetail.py
# @Project :    PositionRecommend
# @Description:

class JobDetail(object):
    communication_button = '//*[@id="main"]/div[1]/div/div/div[1]/div[3]/div[1]/a[2]'
    communication_button_again = '//*[@id="main"]/div[1]/div/div/div[1]/div[3]/div[1]/a[2]'
    mood_button = '//*[@id="main"]/div[1]/div/div/div[1]/div[3]/div[1]/a[1]'
    job_describe_content = '//*[@id="main"]/div[3]/div/div[2]/div[1]/div[2]'
    job_key_list_content = '//*[@id="main"]/div[3]/div/div[2]/div[1]/ul'
    hr_image_button = '//*[@id="main"]/div[3]/div/div[2]/div[1]/div[3]/div[1]/img'
    hr_name = '//*[@id="main"]/div[3]/div/div[2]/div[1]/div[3]/h2'
    hr_position = '//*[@id="main"]/div[3]/div/div[2]/div[1]/div[3]/div[2]'
    hr_active_time = '//*[@id="main"]/div[3]/div/div[2]/div[1]/div[3]/h2/span'


class CompanyInfo(object):
    company_brief_introduction_content = '//*[@id="main"]/div[3]/div/div[2]/div[4]/div[1]/div'
    company_more_button = '//*[@id="main"]/div[3]/div/div[2]/div[4]/div[1]/a'
    business_information_company_name = ''
    business_information_company_legal_representative = ''
    business_information_company_start_time = ''


class DetailPage(JobDetail, CompanyInfo):
    pass
