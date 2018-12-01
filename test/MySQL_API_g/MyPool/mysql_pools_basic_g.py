# -*-coding:utf-8 -*-
# File :mysql_pools_g.py
# Author:George
# Date : 2018/11/30
"""
    python编程中可以使用pymysql进行数据库连接及增删改查操作，但每次连接mysql请求时，都是独立的去请求访问，比较浪费资源，而且访问数量达到一定数量时，对mysql的性能会产生较大的影响。因此实际使用中，通常会使用数据库的连接池技术，来访问数据库达到资源复用。
    python 的数据库连接池包 DBUtils
    DBUtils 提供两种外部接口
    1 PersistentDB: 提供线程专用的数据库连接，并自动管理连接
    2 PooledDB: 提供线程间可共享的数据库连接 并自动管理连接
"""
import pymysql
from DBUtils.PooledDB import PooledDB


# 实例化mysql 连接池对象
def create_pool():
    pool = PooledDB(pymysql, 5, host='127.0.0.1', user='root', passwd='123456', db='test_sqlpool', port=3306)
    return pool


pool = create_pool()

# 以后每次需要连接数据库只需要用connection()方法就可以了
conn = pool.connection()

# 创建游标对象
cursor = conn.cursor()

# 需要执行的SQL语句
SQL = 'select * from tb_student'
# 游标执行查询动作
cursor.execute(SQL)
# 将查询结果返回
result = cursor.fetchall()
print(result)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
