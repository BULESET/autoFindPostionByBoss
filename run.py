# @Time :       30.10.23 12:04 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       run.py
# @Project :    autoFindPositionByBoss
# @Description:

from core.service.src.boss.operation.search import SearchJobPageOperation
from common.driver import driver
import time

if __name__ == '__main__':
    browser = driver()
    search_instance = SearchJobPageOperation(browser)
    search_instance.start(job_name=['移动端测试工程师', '软件测试工程师', '自动化测试工程师'], salary='between_10k_to_20k')
    time.sleep(3)
