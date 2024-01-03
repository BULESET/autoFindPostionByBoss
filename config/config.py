from configparser import ConfigParser
from loguru import logger
from config.enum_env import GetGoldnetEnv
import os
import threading


class Config:

    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

    config = ConfigParser()

    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Config, "_instance"):
            with Config._instance_lock:
                if not hasattr(Config, "_instance"):
                    Config._instance = object.__new__(cls)
        return Config._instance

    def __init__(self):

        if not os.path.exists(self.conf_path):
            logger.error("配置文件不存在！")
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')

    @classmethod
    def get_mysql_db_config(cls, env: str):
        if env not in GetGoldnetEnv().get_type(env='env'):
            logger.info('get_mysql_db_config 传参有误：{}'.format(env))
            return

        rst = {}
        for name, parm in cls.config.items(env + '_mysql_db_conf'):
            rst[name] = parm

        return rst

    @classmethod
    def _get_config(cls, title: str, value: str):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return cls.config.get(title, value)

    @classmethod
    def _set_config(cls, title: str, value: str, text: str):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        cls.config.set(title, value, text)
        with open(cls.conf_path, "w+") as f:
            return cls.config.write(f)

    @classmethod
    def _add_config(cls, title: str):
        """
        配置文件添加
        :param title:
        :return:
        """
        cls.config.add_section(title)
        with open(cls.conf_path, "w+") as f:
            return cls.config.write(f)

    @classmethod
    def _get_keys(cls, title: str):
        i = 0
        data = cls.config.items(title)
        count = len(data)
        names_list = []
        for name, key in data:
            i = i + 1
            names_list.append(name)
            if i >= count:
                return names_list

    @classmethod
    def _get_values(cls, title: str):
        values_list = []
        i = 0
        data = cls.config.items(title)
        count = len(data)
        for name, key in data:
            i = i + 1
            if i < count:
                values_list.append(key)
            else:
                return values_list


if __name__ == '__main__':
    t = Config().get_mysql_db_config("test")
    print(t)
