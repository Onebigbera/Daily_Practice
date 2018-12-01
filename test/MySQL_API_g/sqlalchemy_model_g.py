# -*-coding:utf-8 -*-
# File :sqlalchemy_model_g.py
# Author:George
# Date : 2018/11/30
"""
    Object-Relational Mapping，把关系数据库的表结构映射到对象 在Python中，最有名的ORM框架是SQLAlchemy。我们来看看SQLAlchemy的用法。
"""
from test.MySQL_API_g.sqlalchemy_test_g import *


# 定义user表
class User(Base):
    # 定义其在数据库中名称
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 一对多 关联起来
    books = relationship('Book')


# 建立Book模型  和 User模型是一对多关系
class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 多的一方的book是通过外键关联到user表的
    user_id = Column(String(20), ForeignKey(User.id))


session = create_session()

# 创建新用户
"""
    获取session 把对象添加到session 然后提交并关闭。Session对象可以视为当前数据连接
    
"""

# 将用户对象添加到session中   不是通过操作SQL语句  实现了操作对象 来操作数据库
# session.add(user1)
#
# 提交即保存到数据库
# session.commit()
# 关闭session
# session.close()
# 单条记录查询

# 创建多个用户
user1 = User(id='1', name='jack')
user2 = User(id='2', name='mike')
user3 = User(id='3', name='java')
user4 = User(id='4', name='python')
user6 = User(id='6', name='c++')
user7 = User(id='7', name='c#')
user_list = [user1, user2, user3, user4, user6, user7]

# 批量添加用户
# add_records(session, user_list)

book1 = Book(id='1', name='history', user_id='1')
book2 = Book(id='2', name='music', user_id='1')
book3 = Book(id='3', name='painting', user_id='3')
book4 = Book(id='4', name='chinese', user_id='2')
book5 = Book(id='5', name='chinese', user_id='4')

# add_records(session, [book1, book2, book3, book4, book5])

user = session.query(User).filter(User.id == 1).one()
print(type(user))  # <class '__main__.User'>
print(f'name:{user.name}')
# 记得按照需求处理
print(user.books[0].name)
session.close()
