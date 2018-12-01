# -*-coding:utf-8 -*-
# File :find_file_style.py
# Author:George
# Date : 2018/11/25

"""
    利用os模块对文件的操作 寻找出特定文件夹下的特定类型文件
"""
import os

print(os.getcwd())

FILE_PATH = '\Python_guide\Daily_Practice\test'


# def getPyFile(dirname):
#     flist = os.listdir(dirname)
#     print(flist)
#     pyFileList = []
#     #  遍历当前目录下的一级文件
#     for name in flist:
#         # 把文件名拼接成一个路径
#         filepath = FILE_PATH + "/" + name
#         # 判断遍历到的是一个文件而且是一个Py文件
#         if os.path.isfile(filepath) and name.endswith(".py"):
#             pyFileList.append(name)
#         # 判断遍历到的是一个文件但是不是py文件
#         elif os.path.isfile(filepath) and not name.endswith(".py"):
#             print("%s不是一个py文件" % (name))
#
#         elif os.path.isdir(filepath):##还要判断其是否为路径，如果为真才执行
#             # print("继续做同样的事情")
#             递归遍历
#             pyFileList += getPyFile(filepath)
#     return pyFileList
# pyfile = getPyFile(FILE_PATH)
#
# for path in pyfile:
#     print(path) ##遍历pyfile