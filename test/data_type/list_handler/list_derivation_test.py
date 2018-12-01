# -*-coding:utf-8 -*-
# File :list_derivation_test.py
# Author:George
# Date : 2018/11/24
"""
    列表推导式 语言简洁 速度快 语法精炼
    schedule [expr for value in collection if condition ]
"""
# 需求:找出列表中名称长度大于3的人员
Names = ['bob', 'tom', 'michael', 'jordan', 'george']
list = [name.title() for name in Names if len(name) > 3]
print(list)

# 需求: 将列表中长度大于4的字母大写 长度小于4的小写 在exp 中依旧可以用逻辑
name_list = ['Bob', 'tom', 'Alice', 'Jerry', 'Wendy', 'Smith', 'jack']
result = [name.upper() if len(name) > 4 else name.lower() for name in name_list]
print(result)

# 需求 : 求(x, y) x 是0-5之间的偶数， y是0-5之间的奇数
list_tuple = [(x, y) for x in range(6) if x % 2 == 0 for y in range(6) if y % 2 == 1]
print(list_tuple)

# 生成全排列['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
result_v2 = [m + n for m in 'ABC' for n in 'XYZ']
print(result_v2)
# 需求 求M中3 6 9组成的数列 按需索求
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [x[2] for x in M]
result_v1 = [M[i][2] for i in range(3)]
print(result)
print(result_v1)

# 求M中斜线1 5 9 组成的列表
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [M[i][i] for i in range(len(M))]
print(result)

# 求M, N中矩阵
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
result = [M[row][col] * N[row][col] for row in range(len(M)) for col in range(len(N))]
print(result)

# 也可以加上列表进行循环
result_list = [[M[row][col] * N[row][col] for col in range(len(N))] for row in range(len(M))]
print(result_list)

# 另外一种策略
result_list_v1 = [[M[row][col] * N[row][col] for row in range(len(N))] for col in range(len(M))]
print(result_list_v1)

# 利用列表推导式列出当前目录下的文件和目录名
import os

direct_result = [d for d in os.listdir('.')]
print(direct_result)

# 需求

"""
    嵌套列表推导式
"""

# 需求 将下面的3*4的矩阵交换行和列 | 关键是遍历顺序
M = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
list_exchange = [[row[i] for row in M] for i in range(len(M))]
print(list_exchange)

# 需求 一个男人列表和女人列表组成的嵌套列表 取出姓名中带有两个以上字母'e'姓名，组成列表
namesList = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
             ['Alice', 'Jill', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# 在筛选条件中嵌套 筛选
"""
    遍历名称列表 得到男人和女人的列表 在分别遍历男人和女人的历列表  找出符合条件的名称 先遍历第一层 --》再 遍历的二层 --》
"""
name_req = [name for names in namesList for name in names if name.count('e') >= 2]
print(name_req)
