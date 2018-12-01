# -*-coding:utf-8 -*-
# File :string_handler.py
# Author:George
# Date : 2018/11/24
"""
    string dispose
"""

"""
     sting[start:end:step] 切片操作
"""
string_test = 'manipulation'

# print(string_test[2:3])

# 返回None
# print(string_test[2:3:-1])

# 倒转字符串 notalupinam
# print(string_test[::-1])

# noitalupinam 倒换字符串
# print(string_test[-1::-1])

# 从索引值为-2开始取 on
# print(string_test[-2::])

# 从索引值为-1开始取 正向取值 n
# print(string_test[-1::])

# 当步长为-值时 [A:B:-1] A的默认值为-1 从右边开始取值
# no
print(string_test[:-3:-1])
# no
print(string_test[-1:-3:-1])
# None
print(string_test[0:-3:-1])

# 验证 None
print(string_test[-4:-2:-1])