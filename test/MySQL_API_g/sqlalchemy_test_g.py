# -*-coding:utf-8 -*-
# File :sqlalchemy_test_g.py
# Author:George
# Date : 2018/11/30

"""
    数据库是一个二维表，包含多行多列。
    采用sqlalchemy定义实体类 进行ORM操作
    所谓ORM，就是把复杂的SQL语句给包装成更加面向对象，易于理解的样子.在操作数据库的时候，我们可以用比较底层的MySQLdb之类的模块来直接连接执行SQL语句，但是在实际开发过程中，开发人员一次次写SQL也是很烦的，ORM就是一个解决之道。

"""
# 连接数据库 通过引擎实现
from sqlalchemy import create_engine, Column, String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

# 建立连接信息的映射字典
MYSQL_DB_MAP = {
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'test_sqlalchemy'
}

# 连接配置为: "mysql+pymysql://user:password@host:port/database_name"  注意内部使用了单引号  外面不要用单引号
mysql_conn_str = f"mysql+pymysql://{MYSQL_DB_MAP['user']}:{MYSQL_DB_MAP['password']}@{MYSQL_DB_MAP['host']}:{MYSQL_DB_MAP['port']}/{MYSQL_DB_MAP['database']}"

# 通过连接创建引擎 建立与数据库连接
# 数据库类型 + 数据库驱动名称://用户名:密码@机器地址:端口/数据库名
engine = create_engine(mysql_conn_str, max_overflow=5)

# 创建对象的基类
Base = declarative_base()


# 定义初始化数据库函数 orm同步
def init_db():
    Base.metadata.create_all(engine)


"""
    将orm类映射到DB数据库中 产生DB表
"""


def create_session():
    init_db()
    # 创建数据库Session类型
    Session = sessionmaker(bind=engine)
    # 创建session对象
    session = Session()
    return session

"""
    添加数据
    objs --- 传入的ORM类对象或者对象列表
    objs -(1) obj = Book(book_title=xxx, image=xxx...)
          (2) [obj1, obj2, obj3...]
          
"""

def add_records(session, objs):
    if isinstance(objs, list):
        session.add_all(objs)
    else:
        session.add(objs)
    session.commit()

"""
    查询数据
"""
def query_records(session, Cls, conditions=None):
    if conditions == None:
        return session.query(Cls).all()
    return session.query(Cls).filter_by(conditions).all()
