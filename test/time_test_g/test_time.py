# -*-coding:utf-8 -*-
# File :test_time.py
# Author:George
# Date : 2018/11/24

"""
    time module 时间戳 timestamp(时间戳) 时间戳表示的从1970年1月1日00:00:00开始按秒计算的偏移量。timestamp返回的float类型
"""

import time

# 打印当前时间戳
print(time.time())
print(type(time.time()))

# 打印当前结构化时间
print(time.localtime(time.time()))

# 默认为打印当前时间 param 为时间戳
print(time.localtime())

# global utc utc（世界统一时间，世界标准时间，国际协调时间，简称UTC
# ）时区加上second（时间戳）转换结构化时间，不加则显示当前的结构化时间
print(time.gmtime())

# 结构化时间转化为时间戳
print(time.mktime(time.localtime()))

# 加上时间戳转换为时间戳的格式化时间，不加则返回当前的格式化时间
print(time.ctime())

# 加参数是一个结构化时间 把加的结构化时间转换为结构化时间 不加则返回当前的格式化时间
print(time.asctime())
print(time.asctime(time.gmtime()))

# time.strftime() 将一个结构化时间转化为相应的格式时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 把相应的格式时间，转化为结构化时间
print(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),'%Y-%m-%d %H:%M:%S'))

# time.sleep() 将程序延迟到指定秒数运行 定时器
time.sleep(5)

# time.clock() Unix上返回进程时间 秒 浮点数 windows系统上表示的是进程运行的时间时间 再次调用是第一次调用到现在的时间
print(time.clock())



