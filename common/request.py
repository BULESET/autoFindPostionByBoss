"""
封装request

"""

import os
import random
import requests
from requests_toolbelt import MultipartEncoder
from mime import MimeType
from loguru import logger


class Request:

    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self, https_enable=True):
        """

        :param https_enable:
        """

        self.https_enable = https_enable

    def _enable_https(self, url):

        if self.https_enable:
            if not url.startswith('https://'):
                url = '%s%s' % ('https://', url)
        else:
            if not url.startswith('http://'):
                url = '%s%s' % ('http://', url)
        return url

    @staticmethod
    def _check_header_type(header):
        types = ["application/x-www-form-urlencoded", "application/json", "text/xml", "multipart/form-data"]
        for v in header.values():
            if types[0] in v:
                return types[0]
            if types[1] in v:
                return types[1]

            if types[2] in v:
                return types[2]

            if types[3] in v:
                return types[3]
            else:
                return types[1]

    def send_request(self, method, url, data, header, file_path=None):
        new_method = method.lower()
        if new_method == 'post':
            if self._check_header_type(header) == 'multipart/form-data':
                return self.post_request_multipart(url, data, header, file_path)
            else:
                return self.post_request(url, data, header)

        if new_method == 'get':
            return self.get_request(url, data, header)

    def get_request(self, url, data, header):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        url = self._enable_https(url)
        header_type = self._check_header_type(header)

        try:
            if data is None:
                response = requests.get(url=url, headers=header)
                logger.info("请求返回结果:{}".format(response.json()))
                return response

            elif header_type == "application/x-www-form-urlencoded":
                response = requests.get(url=url, data=data, headers=header)
                return response

            elif header_type == "application/json":
                response = requests.get(url=url, json=data, headers=header)
                # logger.info("请求返回结果:{}".format(response.json()))
                return response

        except requests.RequestException as e:
            logger.error("请求的header:{}".format(header))
            logger.error("请求的body:{}".format(data))
            logger.error("请求的url:{}".format(url))
            logger.error("请求的方法:{}".format("get"))
            logger.error("请求出现错误,请检查接口是否按照接口文档定义发起请求")

            raise

    def post_request(self, url, data, header):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        url = self._enable_https(url)
        header_type = self._check_header_type(header)

        try:
            if data is None:
                logger.info("请求的header:{}".format(header))
                logger.info("请求的body:{}".format(data))
                logger.info("请求的url:{}".format(url))
                logger.info("请求的方法:{}".format("post"))
                response = requests.post(url=url, headers=header)
                return response
            elif header_type == "application/x-www-form-urlencoded":
                logger.info("请求的header:{}".format(header))
                logger.info("请求的body:{}".format(data))
                logger.info("请求的url:{}".format(url))
                logger.info("请求的方法:{}".format("post"))
                response = requests.post(url=url, data=data, headers=header)
                return response

            elif header_type == "application/json":
                logger.info("请求的header:{}".format(header))
                logger.info("请求的body:{}".format(data))
                logger.info("请求的url:{}".format(url))
                logger.info("请求的方法:{}".format("post"))
                response = requests.post(url=url, json=data, headers=header)
                return response

        except requests.RequestException as e:
            logger.error("请求的header:{}".format(header))
            logger.error("请求的body:{}".format(data))
            logger.error("请求的url:{}".format(url))
            logger.error("请求的方法:{}".format("post"))
            logger.error(f"请求出现错误,错误信息{e}")
            raise

    def post_request_multipart(self, url, data, header, file):
        """

        :param url:
        :param data:
        :param header:
        :param file:
        :return:
        """

        url = self._enable_https(url)

        try:
            if data is None:
                response = requests.post(url=url, headers=header)
                return response
            else:
                f_types = str(os.path.basename(file)).split(".")[1]
                f_type = MimeType.get_type(f_types)
                file_path = os.path.join(self.path_dir, file)
                data["file"] = os.path.basename(file_path), open(file_path, 'rb'), f_type
                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                response = requests.post(url=url, data=enc, headers=header, timeout=1000)
                return response

        except requests.RequestException as e:
            logger.error("请求出现错误,请检查接口是否按照接口文档定义发起请求")
            raise

    def put_request(self, url, data, header):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        url = self._enable_https(url)
        try:
            if data is None:
                response = requests.put(url=url, headers=header)
            else:
                response = requests.put(url=url, json=data, headers=header)

        except requests.RequestException as e:
            logger.error("请求出现错误,请检查接口是否按照接口文档定义发起请求")
            raise


if __name__ == '__main__':
    pass
