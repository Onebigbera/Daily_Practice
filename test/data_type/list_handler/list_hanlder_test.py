# -*-coding:utf-8 -*-
# File :list_hanlder_test.py
# Author:George
# Date : 2018/11/24

# 列表常见操作
list = [1, 2, 3, 4, 5]

# 在末尾追加
list.append(6)

# 扩展元素 list.extend(self, iterable_object)
# list.extend([7, 8, 9])
list.extend((7, 8, 9))
print(list)

# insert(self, index, object) 在具体索引位置添加元素
list.insert(5, 10)
print(list)

# index(self, object, start,stop) 在固定索引区间寻找某个字符得索引
print(list.index(10))

# pop 删除 默认删除最后一个 pop(self, index) 按照索引删除
list.pop()
list.pop(5)
print(list)

# remove(self, object) 默认删除第一个
list.remove(8)
print(list)

# 统计列表中元素数量 count(object)
print(list.count(3))

# reverse(self) 将原列表元素倒序排放
list.reverse()
# [7,6,5,4,3,2,1]
print(list)
print(list[2])

# sort(self ,key) 对列表加逆行排序整理 按照顺序整理
list.sort()
print(list)

# sorted(iterable, key , reverse) 高阶函数 既可以保留原列表 又能得到已经排序好得列表 参数是一个列表
list1 = sorted([5,4,7,3,1,8])
print(list1)