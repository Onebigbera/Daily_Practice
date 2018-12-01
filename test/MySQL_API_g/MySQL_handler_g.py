# -*-coding:utf-8 -*-
# File :MySQL_handler_g.py
# Author:George
# Date : 2018/11/30
"""
    模仿写一个对应的pymysql的API  使用pymysql 模块
"""

# --------------python 控制mysql的API-----------------
import pymysql


# 创建数据库连接对象
def init_connect():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test_sql',
                           charset='utf8')
    # 创建游标对象
    cursor = conn.cursor()
    return (conn, cursor)


def close(conn, cursor):
    # 关闭游标
    cursor.close()
    # 断开连接
    conn.close()


"""
    SQL 语句查询
"""


def query_record(cursor, sql):
    # 游标执行sql
    cursor.execute(sql)
    # 将游标执行的结果捎回
    result = cursor.fetchall()
    return result


"""
    SQL语句插入
    批量插入
    values:[(),(),()]
"""


def add_record(conn, cursor, sql, values=[]):
    try:
        # 先判断values的类型
        if isinstance(values, list):
            cursor.executemany(sql, values)
            # 提交事务
            conn.commit()
            return True
        # 否则sql为单条sql语句
        sql = sql % values
        print(sql)
        cursor.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        # 将错误打印出来
        print(e)
        # 事务回滚
        conn.rollback()
        return False

if __name__ == "__main__":
    # 初始化连接和游标 以元祖变量 来接收返回的双元素元祖 而且原酸元素不可改变
    (conn, cursor) = init_connect()
    # sql为单条语句时
    sql = "insert into tb_user(name, address) values('%s', '%s')"

    #需要插入大量的values时候

    values = ('steven_3', 'England')
    """
        特别需要注意的是当values为单条插入数据时，sql 语句中的 %s 需要加上'' 才能正常执行
        而当values 为多组数值时，%s 不管字段是什么类型，占位符%s都不能加上 '' 
        添加的数据格式必须为 tuple(tuple(), tuple(),...) 或者 list[tuple(),tuple()...]
    """
    # values = [('lulu', 'china'),('joke', 'korean'),('hanks', 'japan')]
    if not add_record(conn, cursor,sql,values):
        print("插入数据失败！")
        close(conn, cursor)
        exit()
    print("插入数据成功！")

    # 查询语句
    sql = 'select * from tb_user'
    result = query_record(cursor,sql)
    print(result)

# 实际上我们可以按照% 的连接方法 将数据按照固定格式传入值
#     string = 'insert into tb_user(id, name, address) VALUES(%s, %s, %s)'
#     values = ('7', '刘德华', 'china')
#     print(string % values)





