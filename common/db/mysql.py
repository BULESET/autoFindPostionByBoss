# -*- coding: utf-8 -*-
"""
@作者:  sunyong
@文件:  mysql.py
@时间:  2022/08/03
@描述:

"""
import pymysql
import urllib.parse
from loguru import logger
from config.Config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from sqlalchemy.engine import reflection


class MySql(object):

    def __init__(self, env=None):
        self.conn = None
        self.query = None
        self.db_conf = Config()
        self._db_session = None
        self.engine = None
        self.db_config = None
        self.env = env
        self._use_orm = False

    #
    # def __enter__(self):
    #     return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.query.close()
    #     logger.info('关闭MySQL数据库')
    #     self.conn.close()

    def __del__(self):
        try:
            if self._use_orm:
                logger.info(f'使用ORM框架')
                self._db_session.close()
                logger.info(f'数据库连接已经断开')
                self.engine.dispose()
                logger.info('数据库连接已关闭')
            else:
                logger.info(f'未使用ORM框架')
                self.query.close()
                self.conn.close()
                logger.info(f'【数据库连接已经断开】')
                logger.info('数据库连接已关闭')
        except (Exception,) as e:
            logger.error('关闭数据库连接异常')

    def connect_db(self, db_name=None, use_orm=False, env=None):
        """

        :param db_name:
        :param use_orm:
        :param env:
        :return:
        """
        logger.info(f'【链接MySQL数据库】')
        if self.env:
            self.db_config = self.db_conf.get_mysql_db_config(env=self.env)
        else:
            self.db_config = self.db_conf.get_mysql_db_config(env=env)

        if not use_orm:
            self.conn = pymysql.connect(
                host=self.db_config["host"],
                user=self.db_config["user_name"],
                passwd=self.db_config["password"],
                database=db_name,
                port=int(self.db_config["port"]),
                charset="utf8mb4",
                # use_unicode=True,
                cursorclass=pymysql.cursors.DictCursor
            )
            return self.conn
        else:
            self._use_orm = True
            if db_name:
                connection_info = 'mysql+pymysql://' + self.db_config['user_name'] + ':' + urllib.parse.quote_plus(
                    self.db_config['password']) + '@' + self.db_config['host'] + ':' + self.db_config[
                                      'port'] + '/' + db_name

                self.engine = create_engine(connection_info, poolclass=NullPool)
                DBSession = sessionmaker(bind=self.engine)
                self._db_session = DBSession()
                return self._db_session
            else:
                raise Exception('使用ORM框架必须传入db_name参数')

    def query_sql(self, sql, *args, **kwargs):
        self.query = self.conn.cursor()
        self.query.execute(sql, *args, **kwargs)
        query_result = self.query.fetchall()
        return query_result

    def insert_sql(self, sql, *args, **kwargs):

        self.query = self.conn.cursor()
        logger.info(f'insert_sql:{sql}')
        self.query.execute(sql, *args, **kwargs)
        self.conn.commit()

    def delete_sql(self, sql, *args, **kwargs):

        self.query = self.conn.cursor()
        logger.info(f'delete_sql:{sql}')
        self.query.execute(sql, *args, **kwargs)
        self.conn.commit()

    def update_sql(self, sql, *args, **kwargs):

        self.query = self.conn.cursor()
        self.query.execute(sql, *args, **kwargs)
        self.conn.commit()

    def roll_back(self):
        logger.info(f'数据回滚')
        self.conn.rollback()


if __name__ == "__main__":
    mysql_instance = MySql(env='test')
    mysql_instance.connect_db()
    sts = 'select message_body from goldnet_message.goldnet_sms where phone_number = 13546468710 order by  create_time desc  limit 1;'
    rst = mysql_instance.query_sql(sts)
    print(rst)
    # #
    # desc = mysql.query.description
    # for field in desc:
    # #     print(field[0])
    # #
    # with MySql(env='test1') as mysql:
    #     mysql.connect_db()
    #     t = mysql.query_sql(sts)
    #     print(t)
    #
    # mysql_instance = MySql(env='test1')
    # mysql_instance.connect_db(db_name='goldnet_user', use_orm=True)
    # engine = mysql_instance.engine_info
    # insp = reflection.Inspector.from_engine(engine)
    # colums = insp.get_columns('goldnet_outuser_bind')  # 这里是写的表名
    # for i in colums:
    #     print(i)
    pass
