# @Time :       3.1.24 9:54 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       search.py
# @Project :    PositionRecommend
# @Description:


class SearchResultList(object):
    search_result_list = '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul'
    job_name = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-title clearfix"]/span[@class="job-name"]'
    job_area = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-title clearfix"]/span[@class="job-area-wrapper"]//span[@class="job-area"]'
    job_salary = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-info clearfix"]/span[@class="salary"]'
    hr_online = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-info clearfix"]//span[@class="boss-online-tag"]'
    company_name = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-card-right"]//div[@class="company-info"]//h3[@class="company-name"]//a'
    company_tag_list = '//div[@class="page-job-inner"]//div[@class="page-job-content clearfix"]//div[@class="job-list-wrapper"]//div[@class="search-job-result"]//div[@class="job-card-body clearfix"]//div[@class="job-card-right"]//div[@class="company-info"]//ul[@class="company-tag-list"]'
    search_page = '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/div/div/div/a'


class SearchCondition(object):
    search_box = '//*[@id="wrap"]/div[2]/div[1]/div[1]/div/div/div/input'
    search_button = '//*[@id="wrap"]/div[2]/div[1]/div[1]/div/a'
    area_select_button = '//*[@id="wrap"]/div[2]/div[1]/div[1]/div/span'
    city_list = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/ul/li'
    area_of_city = '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/ul/li'


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
