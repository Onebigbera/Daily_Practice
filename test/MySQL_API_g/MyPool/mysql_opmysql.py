# -*-coding:utf-8 -*-
# File :mysql_opmysql.py
# Author:George
# Date : 2018/11/30

"""
    利用pymysql 和 DBUtils 建立起的mysql 数据库连接包工具
    单例模式用上去
"""
import pymysql
from DBUtils.PooledDB import PooledDB
from test.MySQL_API_g.MyPool.mysqlinfo import mysqlInfo


class MyPool(object):
    __pool = None

    def __init__(self):
        """
        构建函数 构建数据库连接、游标对象
        """
        self.conn = MyPool.get_conn()
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    @staticmethod
    def get_conn():
        """
        建立起数据库池连接、返回数据库池游标对象
        :return:
        """
        if MyPool.__pool is None:
            # 创建连接对象
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=5, host=mysqlInfo['host'], user=mysqlInfo['user'],
                              passwd=mysqlInfo['passwd'], db=mysqlInfo['db'], port=mysqlInfo['port'],
                              charset=mysqlInfo['charset'])
        return __pool.connection()

    def add_record(self, sql, values=[]):
        """

        :param sql: 需要执行的sql 执行sql的值
        :param values:
        :return:
        """
        try:
            # 批量插入
            if isinstance(values, list):
                self.cursor.excutemany(sql, values)
                self.conn.commit()
                return True
            # 单条执行
            sql = sql % values
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False

    def query_record(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()

    def __del__(self):
        del self


if __name__ == "__main__":
    pool = MyPool()
    sql = "insert into tb_student(id,name)values('%s','%s')"
    values = (2, 'google')

    # 查询结果测试
    sql_1 = "select * from tb_student"
    result = pool.query_record(sql_1)
    print(result)

    # 插入结果测试
    if not pool.add_record(sql, values):
        print('数据插入失败')
        pool.close()
        exit()
    print('数据插入成功')
