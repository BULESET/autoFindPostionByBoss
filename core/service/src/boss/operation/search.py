# @Time :       4.1.24 2:46 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       search.py
# @Project :    PositionRecommend
# @Description:

from core.service.src.boss.pages.search import Search
from common.driver import driver

url = 'https://www.zhipin.com/web/geek/job'


class SearchJobPageOperation(object):
    page = driver()

    def __init__(self, searchJobPageUrl):
        self.url = searchJobPageUrl

    def search(self):
        self.page.goto(self.url)
        self.page.wait_for_timeout(4000)
        print(Search().search_job.search_box)

    def find_job_name(self, job_name: str) -> list:
        """
        返回的列表页中寻找工作名称
        :param job_name:
        :return:
        """
        job_name_list = []
        job_name_result_list = self.page.query_selector_all(Search().search_job.job_name)
        for index, value in enumerate(job_name_result_list):
            if job_name == value.text_content():
                job_name_list.append(index)

        return job_name_result_list

    def find_job_salary(self, job_salary: str) -> list:
        """
        返回的列表页中寻找工作范围
        :param job_salary:
        :return:
        """
        job_salary_list = []
        job_salary_result_list = self.page.query_selector_all(Search().search_job.job_salary)
        for index, salary in enumerate(job_salary_result_list):
            if job_salary == salary.text_content():
                job_salary_list.append(index)

        return job_salary_list

    def find_job_area(self, job_area: str) -> list:
        """
        返回的列表页中查找工作区域
        :param job_area:
        :return:
        """
        job_area_list = []
        job_salary_result_list = self.page.query_selector_all(Search().search_job.job_area)
        for index, area in enumerate(job_salary_result_list):
            if job_area == area.text_content():
                job_area_list.append(index)
        return job_area_list

    def find_hr_online(self) -> list:
        """
        返回的列表页中寻找hr在线数据
        :return:
        """
        hr_online_list = []
        hr_online_result_list = self.page.query_selector_all(Search().search_job.hr_online)
        for index, online_result in enumerate(hr_online_result_list):
            if "在线" == online_result.text_content():
                hr_online_list.append(index)
        return hr_online_list

    def find_company_name(self, company_name: str) -> list:
        """
        返回的列表页中寻找工作名称
        :param company_name:
        :return:
        """
        company_name_list = []
        company_name_result_list = self.page.query_selector_all(Search().search_job.company_name)
        for index, company_name_result in enumerate(company_name_result_list):
            if company_name == company_name_result.text_content():
                company_name_list.append(index)
        return company_name_list

    def find_city(self, city_name: str) -> list:
        """
        顶部查询城市
        :param city_name:
        :return:
        """
        city_name_list = []
        city_name_result_list = self.page.query_selector_all(Search().search_job.city_list)
        for index, city_name_result in enumerate(city_name_result_list):
            if city_name == city_name_result.text_content():
                city_name_list.append(index)
        return city_name_list

    def find_area_of_city(self, area_name: str) -> list:
        """
        顶部查询城市对应下的区域
        :param area_name:
        :return:
        """
        rea_of_city_list = []
        area_of_city_result_list = self.page.query_selector_all(Search().search_job.area_of_city)
        for index, area_of_city_result in enumerate(area_of_city_result_list):
            if area_name == area_of_city_result.text_content():
                rea_of_city_list.append(index)
        return rea_of_city_list

    def click_city(self):
        pass

    def click_area_of_city(self):
        pass

    def click_job_card(self, index: [list[int, str], int, str], pause_time: [int] = 8000):
        """

        :param index:
        :param pause_time:点击后停留的时长,单位毫秒,默认8秒
        :return:
        """

        if isinstance(index, (int, str)):
            index = '[' + str(index) + ']'
            element = Search().search_job.search_result_list + '/li' + index
            self.page.click(element)
            self.page.wait_for_timeout(pause_time)
            return self.page.url, index


if __name__ == '__main__':
    S = SearchJobPageOperation(url)
    S.search()
