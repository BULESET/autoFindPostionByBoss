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
    chat_list_bottom = '//*[@id="container"]/div/div/div[1]/div/div[3]/div/div/div[1]/div/div'


class ChatDetail(object):
    pass


class ChatPage(ChatList, ChatDetail):
    pass
