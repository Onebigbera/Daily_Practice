# -*-coding:utf-8 -*-
# File :dict_derivation_test.py
# Author:George
# Date : 2018/11/24
"""
    字典推导式
    字典推导式和列表推导式思想一致 产生数据类型差异
"""
# 按照数字有序建立字典
string = ['this', 'is', 'a', 'dict', 'comprehensions']
# {0: 'this', 1: 'is', 2: 'a', 3: 'dict', 4: 'comprehensions'}
result = {key: value for key, value in enumerate(string)}
print(result)

# 用字典推导式以及字符串及其长度建立字典
s = {string[i]: len(string[i]) for i in range(len(string))}
print(s)
# 直接整体遍历
k = {k: len(k) for k in string}
print(k)

# 将同一个字母但是不同大小写的值合并并以小写形式返回 即使遍历过'a'后再次遍历'A'依然为'a' 值一样 并且会覆盖
calculate_string = {'a': 10, 'b': 21, 'd': 5, 'A': 12, 'B': 12, "C": 4}
result = {key.lower(): calculate_string.get(key.lower(), 0) + calculate_string.get(key.upper(), 0) for key in
          calculate_string.keys()}
print(result)

# 利用字典推导式将字典中的key value对调
roll_book = {'jordan': 0, 'micheal': 1, 'miss': 3, 'jack': 4, 'tom': 5}
# 当两个值遍历时 记得要用dict.items() 是列表中元祖对应 dict默认为遍历key
roll_book_v1 = {value: key for key, value in roll_book.items()}
print(roll_book_v1)
