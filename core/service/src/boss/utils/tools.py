# @Time :       25.3.24 10:37 上午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       tools.py
# @Project :    autoFindPositionByBoss
# @Description:
import os

#
# current_path = os.path.dirname(os.path.abspath('.'))
# login_data_path = os.path.join(current_path, 'tmpFile')
# path = os.path.dirname(__file__)
# pas = os.path.abspath(__file__)
current_path = os.path.dirname(os.path.dirname(__file__))
login_data_path = os.path.join(current_path, 'tmpFile')


def checkoutLoginFile():
    file_list = os.listdir(login_data_path)
    if 'login_data.json' in file_list:
        return True
    else:
        return False


# def deleteLoginFile():
#     loginFilePath = os.path.join(login_data_path, 'login_data.json')
#     os.remove(loginFilePath)


if __name__ == '__main__':
    print(login_data_path)
    print(current_path)
    # print(path)
    # print(pas)
