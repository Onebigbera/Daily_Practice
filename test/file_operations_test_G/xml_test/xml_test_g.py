# -*-coding:utf-8 -*-
# File :xml_test_g.py
# Author:George
# Date : 2018/12/22
"""
    XML即可扩展置标语言（英文：Extensible Markup Language，简称XML），又称可扩展标记语言，是一种置标语言。置标指计算机所能理解的信息符号，通过此种标记，计算机之间可以处理包含各种信息的文章等。它与HTML一样，都是SGML(标准通用标记语言)。XML是Internet环境中跨平台的，依赖于内容的技术，是当前处理结构化文档信息的有力工具。扩展标记语言XML是一种简单的数据存储语言，使用一系列简单的标记描述数据，而这些标记可以用方便的方式建立，虽然XML占用的空间比二进制数据要占用更多的空间，但XML极其简单易于掌握和使用。
"""
"""
    从 XML 文件中获取标签的值
"""
# python 中处理 xml 的模块
from xml.dom import minidom


def parse_xml_g(path):
    # path = r'F:\Python_guide\Daily_Practice\test\file_operations_test_G\xml_test\51zxw.xml'
    # 解析目标 XML 文件 得到 dom 对象
    dom = minidom.parse(path)
    # 获取文档对象元素 得到 根节点树
    root = dom.documentElement

    # 根据标签名称获取标签对象 包含了所有标签名称为 'name' 的标签
    names = root.getElementsByTagName('name')
    ages = root.getElementsByTagName('age')
    cities = root.getElementsByTagName('city')

    # 将取到的节点元素打印出来 如果不加 .firstChild.data 那么能取到对象 但是拿不到具体值
    [print(name.firstChild.data) for name in names]
    [print(age.firstChild.data) for age in ages]
    [print(city.firstChild.data) for city in cities]

    # 获取标签属性节点 如 <login name='student' password='123456'>
    # 先获取对应节点元素
    logins = root.getElementsByTagName('login')
    [print(login.getAttribute('username')) for login in logins]
    [print(login.getAttribute('password')) for login in logins]
    # 获取节点中属性值 注意查看标签
    # username = logins[0].getAttribute('username')
    # print(username)
    # password = logins[0].getAttribute('password')
    # print(password)

def get_node_attr_g(path):

    dom = minidom.parse(path)
    # 获取 根节点树
    root = dom.documentElement
    # 获取所有 student 节点 都是先定位 再获取属性
    students = root.getElementsByTagName('student')
    print(students[0].nodeName)     # student
    print(students[0].nodeType)     # 1
    print(students[0].nodeValue)    # None


if __name__ == "__main__":
    path = r'F:\Python_guide\Daily_Practice\test\file_operations_test_G\xml_test\51zxw.xml'
    # parse_xml_g(path)

    get_node_attr_g(path)