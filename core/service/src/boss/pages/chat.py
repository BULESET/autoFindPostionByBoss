# @Time :       4.1.24 9:54 上午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       chat.py
# @Project :    PositionRecommend
# @Description:

class ChatList(object):
    search_box = '//*[@id="container"]/div/div/div[1]/div/div[1]/div/input'
    search_button = '//*[@id="container"]/div/div/div[1]/div/div[1]/div/div/i'
    chat_type_of_all_button = '//*[@id="container"]/div/div/div[1]/div/div[2]/ul/li[1]'
    chat_type_of_new_chat_button = '//*[@id="container"]/div/div/div[1]/div/div[2]/ul/li[2]'
    chat_type_of_only_chat_button = '//*[@id="container"]/div/div/div[1]/div/div[2]/ul/li[3]/span'
    chat_type_of_has_change_info_button = '//*[@id="container"]/div/div/div[1]/div/div[2]/ul/li[4]/span'
    chat_type_of_has_interview_button = '//*[@id="container"]/div/div/div[1]/div/div[2]/ul/li[5]/span'
    chat_list = '//*[@id="container"]/div/div/div[1]/div/div[3]/div/div'
    chat_selected = '//*[@id="container"]/div/div/div[1]/div/div[3]/div/div/ul[2]/li[1]'
    chat_list_bottom = '//*[@id="container"]/div/div/div[1]/div/div[3]/div/div/div[1]/div/div'


class ChatCommonExpressionsPopupWindow(object):
    chat_common_expressions_popup_window = '//*[@id="container"]/div/div/div[2]/div[3]/div/div[5]'
    chat_common_expressions_popup_window_title = '//*[@id="container"]/div/div/div[2]/div[3]/div/div[5]/div/h3'
    chat_common_expressions_popup_window_settings_button = '//*[@id="container"]/div/div/div[2]/div[3]/div/div[5]/div/a'
    chat_common_expressions_popup_window_expression = '//*[@id="container"]/div/div/div[2]/div[3]/div/div[5]/ul'
    chat_common_expressions_content = '//*[@id="container"]/div/div/div[2]/div[3]/div/div[5]/ul/li'


class ChatListDetail(ChatCommonExpressionsPopupWindow):
    chat_input = '//*[@id="chat-input"]'
    chat_emote_button = ''
    chat_common_expressions_button = '//*[@id="container"]/div/div/div[2]/div[3]/div/div[1]/div[2]'
    send_summary_button = '//*[@id="container"]/div/div/div[2]/div[3]/div/div[1]/div[5]'
    exchange_wechat_button = '//*[@id="container"]/div/div/div[2]/div[3]/div/div[1]/div[7]'
    exchange_phone_number_button = '//*[@id="container"]/div/div/div[2]/div[3]/div/div[1]/div[6]'


class ChatWithHRPopupWindow(object):
    pop_up_window = '.dialog-container'
    pop_up_window_title = '.dialog-container >> .dialog-title'
    pop_up_window_close_button = '..dialog-container >> .dialog-title >> .dialog_close >> .icon-close'
    pop_up_window_close_input_box = '.dialog-container >> .startchat-content >> .edit-area >> .input-area >> .'
    pop_up_window_close_input_send_message_button = '.dialog-container >> .startchat-content >> .edit-area >> .send-message'
    pop_up_window_close_boss_name = '.dialog-container >> .dialog-title >> .startchat-title >> .boss-info >> .name'
    pop_up_window_close_job_name = '.dialog-container >> .dialog-title >> .startchat-title >> .boss-info >> .position'


class ChatPage(ChatList, ChatListDetail, ChatWithHRPopupWindow):
    pass
