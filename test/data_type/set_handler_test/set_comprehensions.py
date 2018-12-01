# -*-coding:utf-8 -*-
# File :set_comprehensions.py
# Author:George
# Date : 2018/11/24
"""
    集合推导式和列表推导式类似 区别在于它使用{}
    保留了集合的特性 去重
"""
# 计算去重
set_test = {x**2 for x in [1, 1, 2, 2, 3]}
print(set_test)

# 统计列表中字符串长度的个数
string = ['jordan', 'micheal', 'black', 'riq', 'miss', 'tom']
len_set = {len(item) for item in string}
print(len_set)
