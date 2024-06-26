# @Time :       3.1.24 9:54 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       search.py
# @Project :    autoFindPositionByBoss
# @Description:


class SearchResultList(object):
    search_result_list = '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul'
    card = '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li'
    job_name = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-title clearfix"]/span[@class="job-name"]'
    job_area = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-title clearfix"]/span[@class="job-area-wrapper"]//span[@class="job-area"]'
    job_salary = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-info clearfix"]/span[@class="salary"]'
    hr_online = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-info clearfix"]//span[@class="boss-online-tag"]'
    company_name = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-card-right"]//div[@class="company-info"]//h3[@class="company-name"]//a'
    company_tag_list = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-card-right"]//div[@class="company-info"]//ul[@class="company-tag-list"]'
    search_page = '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/div/div/div/a'
    salary = '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[index]/div[1]/a/div[2]/span'
    not_limit_button = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[6]/div[2]/ul/li[1]'
    under_3k_button = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[6]/div[2]/ul/li[2]'
    between_3k_to_5k_button = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[6]/div[2]/ul/li[3]'
    next_page_button = '.options-pages >> .ui-icon-arrow-right'
    previous_page_button = '.options-pages >> .ui-icon-arrow-left'
    first_page_button = '#wrap > div.page-job-wrapper > div.page-job-inner > div > div.job-list-wrapper > div.search-job-result > div > div > div > a:nth-child(2)'

    c = 'options-pages'

    def get_chat_button_at_now_element(self, index):
        return self.card + '[' + index + ']' + '/div[1]/a/div[2]/a'

    def get_hr_online_status_element(self, index):
        return self.card + '[' + index + ']' + '/a/div[2]/span[2]'


class SearchCondition(object):
    search_box = '//*[@id="wrap"]/div[2]/div[1]/div[1]/div/div/div/input'
    search_button = '//*[@id="wrap"]/div[2]/div[1]/div[1]/div/a'
    area_select_button = '//*[@id="wrap"]/div[2]/div[1]/div[1]/div/span'
    city_list = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/ul/li'
    area_of_city = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/ul/li'
    select_money_button = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[6]/div[1]/span'
    not_limit_button = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[6]/div[2]/ul/li[1]'
    under_3k_button = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[6]/div[2]/ul/li[2]'
    between_3k_to_5k_button = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[6]/div[2]/ul/li[3]'
    between_5k_to_10k_button = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[6]/div[2]/ul/li[4]'
    between_10k_to_20k_button = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[6]/div[2]/ul/li[5]'
    between_20k_to_50k_button = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[6]/div[2]/ul/li[6]'
    up_50k_button = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[6]/div[2]/ul/li[7]'


class SearchJob(SearchCondition, SearchResultList):
    pass


class SearchCompany(object):
    pass


class Search(SearchJob, SearchCompany):

    @property
    def search_job(self):
        return SearchJob

    @property
    def search_company(self):
        return SearchCompany


if __name__ == '__main__':
    print(Search().search_job.search_box)
