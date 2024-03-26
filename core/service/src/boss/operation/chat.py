# @Time :       25.3.24 5:00 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       chat.py
# @Project :    PositionRecommend
# @Description:

import time

from core.service.src.boss.pages.chat import ChatPage
from core.service.src.boss.utils.tools import checkoutLoginFile
from core.service.src.boss.operation.login import LoginPageOperation
import os


class ChatWithHRListBase(object):
    chat_url = 'https://www.zhipin.com/web/geek/chat'
    current_path = os.path.dirname(os.path.abspath('.'))
    tmp_path = os.path.join(current_path, 'tmpFile', 'login_data.json')

    def __init__(self, browser, content=None, page=None):
        if not checkoutLoginFile():
            self.login_instance = LoginPageOperation(browser)
            self.login_instance.login_by_qr_code()
            self.content = self.login_instance.content
            self.browser = browser
            self.page = self.login_instance.page

        else:
            if not browser.contexts:
                self.content = browser.new_context(storage_state=self.tmp_path)
                self.page = self.content.new_page()

            else:
                self.browser = browser
                self.content = content
                self.page = page


class ChatWithHRListOperation(ChatWithHRListBase):

    def __init__(self, browser, content=None, page=None):
        super().__init__(browser, content=content, page=page)
        self.goToChatPage()

    def goToChatPage(self):
        self.page.wait_for_url(self.chat_url)
        self.page.goto(url=self.chat_url)
        self.page.wait_for_timeout(4000)

    def selectChat(self, select_info):
        pass

    def closePage(self):
        self.page.close()

    def chatWithHR(self):
        pass

    def sendCommonChatText(self):
        self.page.locator(ChatPage().chat_common_expressions_button).click()
        self.page.locator(ChatPage().chat_common_expressions_content).first.click()


class ChatWithHRPopupWindowOperation(ChatWithHRListBase):

    def __init__(self, browser, content=None, page=None):
        super().__init__(browser, content=content, page=page)
        self.dialog_status = self.checkoutDialogWindow()

    def checkoutDialogWindow(self):
        if self.page.url == self.chat_url:
            return False
        if self.page.locator(ChatPage().pop_up_window).is_visible():
            return True
        else:
            return False

    def closePopupWindow(self):
        if self.dialog_status:
            self.page.locator(ChatPage().pop_up_window_close_button).click()

    def input_message(self, message):
        self.page.locator(ChatPage().pop_up_window_close_input_box).fill(message)

    def send_message(self):
        self.page.locator(ChatPage().pop_up_window_close_input_send_message_button).click()

    def get_boss_name(self):
        return self.page.locator(ChatPage().pop_up_window_close_boss_name).inner_text()

    def get_job_name(self):
        return self.page.locator(ChatPage().pop_up_window_close_job_name).inner_text()

    def get_friend_message(self):
        pass

    def chat(self, myself_message, friend_message):
        self.get_friend_message()
        self.input_message(myself_message)
        self.send_message()




class ChatWithHROperation(ChatWithHRListOperation, ChatWithHRPopupWindowOperation):

    def _get_current_url(self):
        return self.page.url

    def close(self, closePopupPage=False):
        """

        :param closePopupPage: 是否关闭对应弹窗所在的页面，否的话只关闭弹窗，是的话弹窗和页面都会被关闭
        :return:
        """
        if self.dialog_status:
            if not closePopupPage:
                self.closePopupWindow()
            else:
                self.closePopupWindow()
                self.closePage()
        else:
            self.page.wait_for_url(self.chat_url)
            self.closePage()

    def send_common_message(self):
        if self.dialog_status:
            pass
        else:
            self.sendCommonChatText()

    def send_message(self):
        pass

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
    # R = driver()
    # # contexts = browser.new_context()
    # # page = contexts.new_page()
    # # page.goto('http://www.baidu.com')
    # S = ChatWithHRListOperation(R)
    # S.close()
    # time.sleep(10)
