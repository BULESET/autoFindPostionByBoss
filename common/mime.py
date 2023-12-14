# @Time :       15.1.22 9:53 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       mime.py
# @Project :    ApiTest
# @Description:


from enum import Enum


class MIME(Enum):

    acx = "application/internet-property-stream"
    jpe = "image/jpeg"
    jpeg = "image/jpeg"
    jpg = "image/jpeg"
    jfif = "image/pipeg"
    xbm = "image/x-xbitmap"
    pdf = "application/pdf"
    ppt = "application/vnd.ms-powerpoint"
    ps = "application/postscript"
    zip = "application/zip"
    xls = "application/vnd.ms-excel"
    xlm = "application/vnd.ms-excel"
    txt = "text/plain"
    uls = "text/iuls"
    all_type = "application/octet-stream"


class MimeType(object):
    """获取文件MineType"""
    @staticmethod
    def get_type(mime_type):
        member = MIME.__members__.get(mime_type.lower())
        return member.value

