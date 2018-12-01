# -*-coding:utf-8 -*-
# File :delete_space.py
# Author:George
# Date : 2018/12/1
"""
    删除一个字符串中连续超过一次的空格
"""
def del_space(string):
    # 先分割 .split()
    string_split = string.split(' ')
    # 列表生成式筛选出非空字符串项 ' '
    string_list = [i for i in string_split if i != ' ']
    # 再装载添加 ' '
    result_string = ' '.join(string_list)
    print(result_string)
    return result_string

del_space('Hello  mike, nice to meet you!   ')
