# -*-coding:utf-8 -*-
# File :spreadList.py
# Author:George
# Date : 2018/12/3
"""
    sum(*args, **kwargs) 首个参数为可迭代对象(列表、数组等) 第二个参初始值默认为0，也可以为其他值 比如[] 空列表 python中类型动态类型 一种操作或者接口，到底做何种操作取决于对象本身-比如说+ 如果两者都为数字那么 1+1=2 如果两者为字符串 则 '1' +'1' = '11' 所以如果两边都是列表 那么就会实现列表相加
"""
from functools import reduce

list1 = [1, 3, 5]
list2 = [4, 6]
print(sum(list1))
print(sum([list1], []))
print(sum([list1], list2))


# TODO: powerful foo
def spread_list(lst):
    '''
    >>> spread_list([1, 3,[5, 6, [9, 10], [11,[12, [13, 14]]], 15]])
    [1, 3, 5, 6, 9, 10, 11, 12, 13, 14, 15]
    '''
    return sum([spread_list(x) if type(x) is list else [x] for x in lst], [])
    # [[1], [3], [[5], [6], [[9], [10]], [[11], [[12], [[13], [14]]]], [15]]]


# print(spread_list([1, 3,[5, 6, [9, 10], [11,[12, [13, 14]]], 15]]))

# 实现将A = [[1], [2,3], [4,5,6]]二元列表合并成一个一元列表的方法

A = [[1], [2, 3], [4, 5, 6]]

# 方法一 sum()
result = sum(A,[])
print(result)

# 方法二 lambda函数和reduce一起使用
result = reduce(lambda x,y:x+y , A)
print(result)

# 方法三 正则表达式
import re
result_ = [int(i) for i in  re.findall(r'\d', str(A))]
print(result_)

# 方法四 多重遍历迭代   知道数据结构前提下操作
result = []
for num in A:
    for item in num:
        result.append(item)
print(result)


