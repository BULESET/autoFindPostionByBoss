# @Time :       25.3.24 5:00 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       chat.py
# @Project :    autoFindPositionByBoss
# @Description:

import time

from core.service.src.boss.pages.chat import ChatPage
from core.service.src.boss.utils.tools import checkoutLoginFile
from core.service.src.boss.operation.login import LoginPageOperation
from common.driver import driver
from loguru import logger
import os


class ChatWithHRListBase(object):
    chat_url = 'https://www.zhipin.com/web/geek/chat'
    current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tmp_path = os.path.join(current_path, 'tmpFile', 'login_data.json')
    js = "Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});"

    def __init__(self, browser, content=None, page=None):
        if not checkoutLoginFile():
            self.login_instance = LoginPageOperation(browser)
            self.login_instance.login_by_qr_code()
            self.content = self.login_instance.content
            self.browser = browser
            self.page = self.login_instance.page
            self.page.add_init_script(self.js)


        else:
            if not browser.contexts:
                self.content = browser.new_context(storage_state=self.tmp_path)
                self.page = self.content.new_page(no_viewport=True)
                self.page.add_init_script(self.js)


            else:
                self.browser = browser
                self.content = content
                self.page = page
                self.page.add_init_script(self.js)


class ChatWithHRListOperation(ChatWithHRListBase):

    def __init__(self, browser, content=None, page=None):
        super().__init__(browser, content=content, page=page)

    def goToChatPage(self):
        self.page.wait_for_url(self.chat_url)
        self.page.goto(url=self.chat_url)
        self.page.wait_for_timeout(4000)

    def selectChatList(self, select_index=1, **kwargs):
        index = int(select_index)
        chat_count = self.page.locator(ChatPage().chat_list).count()
        if 0 < index <= chat_count and index == 1:
            logger.info('【点击第一个聊天对话内容】')
            self.page.locator(ChatPage().chat_list).first().click()
        if 0 < index <= chat_count:
            logger.info(f'【点击第{index - 1}个聊天对话内容】')
            self.page.locator(ChatPage().chat_list).nth(index - 1).click()

    def closePage(self):
        logger.info('【关闭当前页面】')
        self.page.close()

    def chatWithHR(self):
        pass

    def sendCommonChatText(self):
        logger.info('【点击常用语按钮】')
        self.page.locator(ChatPage().chat_common_expressions_button).click()
        logger.info('【选择打招呼常用语并点击发送】')
        self.page.locator(ChatPage().chat_common_expressions_content).first.click()

    def input_message_in_chat_page_box(self, message):
        self.page.locator(ChatPage().chat_input).fill(message)

    def send_message_in_chat_page_box(self):
        self.page.locator(ChatPage().send_message_button).click()


class ChatWithHRPopupWindowOperation(ChatWithHRListBase):

    def __init__(self, browser, content=None, page=None):
        super().__init__(browser, content=content, page=page)
        self.dialog_type = None
        self.dialog_status = self.checkoutDialogWindow()

    def checkoutDialogWindow(self):
        time.sleep(3)
        logger.info('【检查聊天弹窗是否存在】')
        if self.page.url == self.chat_url:
            logger.info('【聊天弹窗不存在】')
            return False
        if self.page.locator(ChatPage().pop_up_window).is_visible():
            logger.info('【聊天弹窗存在】')
            self.dialog_type = 'chat_window'
            return True
        if self.page.locator(ChatPage().pop_up_window_unable_to_communicate).is_visible():
            logger.info('【今日聊天次数已达到上限】')
            self.dialog_type = 'unable_chat_window'
            return True
        else:
            logger.info('【聊天弹窗不存在】')
            return False

    def closePopupWindow(self):
        if self.dialog_status and self.dialog_type == 'chat_window':
            logger.info('【关闭聊天弹窗】')
            self.page.locator(ChatPage().pop_up_window_close_button).click()
        if self.dialog_status and self.dialog_type == 'unable_chat_window':
            logger.info('【关闭不能聊天弹窗】')
            self.page.locator(ChatPage().pop_up_window_unable_to_communicate_confirm_button).click()

    def input_message_in_pop_window(self, message):
        self.page.locator(ChatPage().pop_up_window_close_input_box).fill(message)

    def send_message_in_pop_window(self):
        self.page.locator(ChatPage().pop_up_window_close_input_send_message_button).click()

    def get_boss_name_in_pop_window(self):
        return self.page.locator(ChatPage().pop_up_window_close_boss_name).inner_text()

    def get_job_name_in_pop_window(self):
        return self.page.locator(ChatPage().pop_up_window_close_job_name).inner_text()

    def get_friend_message(self):
        pass

    def chat(self, myself_message):
        self.get_friend_message()
        self.input_message_in_pop_window(myself_message)
        self.send_message_in_pop_window()


class ChatWithHROperation(ChatWithHRPopupWindowOperation, ChatWithHRListOperation):
    #
    def __init__(self, browser, content=None, page=None):
        logger.info('【ChatWithHROperation初始化】')
        super(ChatWithHROperation, self).__init__(browser, content, page)
        super(ChatWithHRListOperation, self).__init__(browser, content, page)

    def _get_current_url(self):
        return self.page.url

    def close(self, closePopupPage=True):
        """

        :param closePopupPage: 是否关闭对应弹窗所在的页面，否的话只关闭弹窗，是的话弹窗和页面都会被关闭
        :return:
        """
        if self.dialog_status:
            logger.info(f'【dialog_status参数为{self.dialog_status}弹窗存在】')
            if not closePopupPage:
                logger.info(f'【closePopupPage参数为{closePopupPage}关闭聊天弹窗】')
                self.closePopupWindow()
            else:
                logger.info(f'【closePopupPage参数为{closePopupPage}关闭聊天弹窗】')
                self.closePopupWindow()
                logger.info(f'【closePopupPage参数为{closePopupPage}关闭整个页面】')
                self.closePage()
        else:
            self.page.wait_for_url(self.chat_url)
            logger.info(f'【dialog_status参数为{self.dialog_status}弹窗不存在')
            logger.info(f'【关闭整个聊天页面页面】')
            self.closePage()

    def send_common_expressions_message(self, select_index=1):
        if self.dialog_status:
            if self.dialog_type == 'chat_window':
                logger.info(f'【dialog_status参数为{self.dialog_status}弹窗存在')
                self.send_message()
            if self.dialog_type == 'unable_chat_window':
                self.closePopupWindow()
        else:
            logger.info(f'【dialog_status参数为{self.dialog_status}弹窗不存在')
            self.selectChatList(select_index)
            self.sendCommonChatText()

    def send_message(self):
        message = '您好，看了下咱们的招聘岗位描述和我工作经历以及现有的能力比较匹配，想和您聊聊，期待您的回复~'
        if self.dialog_status:
            if self.dialog_type == 'chat_window':
                logger.info(f'【dialog_status参数为{self.dialog_status}弹窗存在')
                logger.info('【聊天弹窗存在】')
                logger.info(f'【点击聊天弹窗并输入打招呼信息】:{message}')
                self.input_message_in_pop_window(message=message)
                self.send_message_in_pop_window()
            if self.dialog_type == 'unable_chat_window':
                return 'unable_chat_today'

        else:
            logger.info('【聊天弹窗不存在,当前页面为聊天页面】')
            logger.info(f'【点击聊天弹窗并输入打招呼信息】:{message}')
            self.input_message_in_chat_page_box(message)
            self.send_message_in_chat_page_box()

    def get_message(self):
        pass

    def input_message(self, massage):
        pass

    def get_job_name(self):
        pass

    def get_boss_name(self):
        pass


if __name__ == '__main__':
    pass
    browser = driver()
    contexts = browser.new_context()
    page = contexts.new_page()
    # ChatWithHROperation(browser).selectChat(select_index=1)
