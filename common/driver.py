# @Time :       3.1.24 7:47 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       driver.py
# @Project :    PositionRecommend
# @Description:

from playwright.sync_api import sync_playwright
from loguru import logger


# from playwright.async_api import async_playwright


def driver():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    return browser


if __name__ == '__main__':
    p = driver()
    print(p)
