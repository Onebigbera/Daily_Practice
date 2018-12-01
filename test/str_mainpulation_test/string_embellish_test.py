# -*-coding:utf-8 -*-
# File :string_embellish_test.py
# Author:George
# Date : 2018/11/24
"""
    常见字符串修饰方法
"""
str = 'optimization'

# str.center(self, width, fillchar) 让字串居中 不能居中左长右短
print(str.center(25, '*'))

# 让字符串在指定长度左对齐
# str.rjust(self, width, fillcahr)
print(str.rjust(32, '!'))
print(str.ljust(32))

# 将字符串补充到指定长度 不足地方补0
print(str.zfill(32))

# format 按照顺序 将参数传递给大括号 传递参数 接收不限个数参数
name = 'george'
age = '18'
print('Hello, i am {}, and i am {} years old'.format(name, age))

print("{0}{1}".format("hello","world"))
print("{0}{1}{1}".format("hello","world")) # helloworldworld

# 关键字传参
print("i'm {name}, age is {age}".format(name='george', age=18))

# 处理文本时 填充经常与对齐一起使用
#  ^ < > 分别代表居中、左对齐、右对齐 后面带宽度 10 :后面带填充的字符串 默认空格填充
print("{:#>18}".format('optimization'))
print("{:^18}".format('optimization'))

# strip 默认去除字符串两边空格
string = '    helllo,world   '
print(string.strip())
# 去除右边空格
print(string.rstrip())
# 去除左边空格
print(string.lstrip())

# 功能型 计数
print(string.count('o'))

# 查找 返回从左边开始第一个指定字符的索引 找不到返回-1
print(string.find('l'))
# return -1
print(string.find('z'))
print(string.rfind('l'))
# -1
print(string.rfind('z'))

# 查找从左边开始第一个指定字符的索引 找不到报错
print(string.index('l'))
# print(string.index('z'))  # ValueError: substring not found
# 从右边开始
print(string.rindex('l'))
# 没找到报错
# print(string.rindex('z'))
