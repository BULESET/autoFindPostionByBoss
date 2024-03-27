# @Time :       3.1.24 9:22 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       index.py
# @Project :    autoFindPositionByBoss
# @Description:

class Navigation(object):
    city_button = '//*[@id="header"]/div[1]/div[2]/p/span[1]'
    index_page_button = '//*[@id="header"]/div[1]/div[3]/ul/li[1]/a'
    recommend_position = '//*[@id="header"]/div[1]/div[3]/ul/li[2]/a'
    search_button = '//*[@id="header"]/div[1]/div[3]/ul/ul[1]/li[1]/a'
    company_button = '//*[@id="header"]/div[1]/div[3]/ul/ul[1]/li[2]/a'
    school_button = '//*[@id="header"]/div[1]/div[3]/ul/ul[2]/li[1]/a'
    sea_turtle_button = '//*[@id="header"]/div[1]/div[3]/ul/ul[2]/li[2]/a'
    app_button = '//*[@id="header"]/div[1]/div[3]/ul/li[3]/a'
    consult_info_button = '//*[@id="header"]/div[1]/div[3]/ul/li[4]/a'
    massage_button = '//*[@id="header"]/div[1]/div[4]/ul/li[1]/a'
    resume_button = '//*[@id="header"]/div[1]/div[4]/ul/span/li/a'
    mine_button = '//*[@id="header"]/div[1]/div[4]/ul/li[2]/a/img'
    login_button = '//*[@id="header"]/div[1]/div[3]/div/a'
    register_button = '//*[@id="header"]/div[1]/div[3]/div/a'
    find_job_button = ' //*[@id="header"]/div[1]/div[3]/div/span/a[2]'
    recruit_button = '//*[@id="header"]/div[1]/div[3]/div/span/a[1]'


class Search(object):
    search_box = '//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/div[2]/p'
    search_button = '//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/button'
    search_map_button = '//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/a'
    job_type_button = '//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/div[2]/div'


class HandPickJob(object):
    pass


class IndexPage(Navigation, Search, HandPickJob):
    pass
