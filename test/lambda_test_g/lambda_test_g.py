# -*-coding:utf-8 -*-
# File :lambda_test_g.py
# Author:George
# Date : 2018/11/25

"""
    lambda 匿名函数的语法只包含一个语句，如下:
    lambda arg1,arg2,arg3...args:express
"""


def sum_test(x, y, z):
    return x + y + z


# lambda函数返回函数对象
sum_g = lambda a, b, c: a + b + c
print(sum_g(1, 2, 3))

# 无参数匿名函数
t = lambda: True
print(t())

# 带参数的匿名函数 允许设置默认值 默认值要放在后面
pow_g = lambda x, y=3: x ** y
print(pow_g(5))

# lambda *z:z *z:允许接收不定长度参数 z为元祖
a = lambda *z: z
print(a('gorge', 'steven'))

# 加上if条件判断 lambda配合三元表达式
print((lambda x, y: x if x > y else y)(101, 100))

# 不需要给函数起名称情况下使用匿名函数优势
print((lambda x: x ** 3)(3))

# 字符串联合
letter = lambda x='Boo', y='Too', z='Zoo': x + y + z
letter('Hello')
print(letter('Hello'))

# lambda函数配合列表联合使用

"""
    匿名函数结合map、filter函数使用发挥其威力
    filter(function, iterable)
"""
result = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8])
# [x for x in [1,2,3,4,5,6,7,8] if x % 3==0]
for i in result:
    print(i)
print(result)  # <filter object at 0x000250c5155>

"""
    lambda 嵌套到普通函数中 lambda函数本身作为return的值
"""


def increment_test(n):
    return lambda x: x + n


# 返回lambda函数对象
print(increment_test(5))  # <function increment_test.<locals>.<lambda> at 0x0000013AC2C837B8>
# 返回lambda函数的返回值
fo = increment_test(5)
result = fo(4)
print(result)

# 和列表联合使用
L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
# 具体调用
print(L[2](2))
for i in L:
    print(i(2))

# 求最小值 结合三元表达式
lower_g = lambda x, y: x if x < y else y
print(lower_g(32, 23))
# 按照ASCLL对应值进行排序
print(lower_g('aa', 'ab'))

# 判断字符串是否以某个字母开头
start_with_gv = lambda string: string.startswith('B')
NAME = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
# 结合filter函数实现 # < filter object >
name_result = filter(start_with_gv, NAME)
print(name_result)

start_with_g = lambda string: True if string[0] == 'B' else False
names = ['Bob', 'Aow', 'Steven']
for i in names:
    print(start_with_g(i))
# 等价于用列表表达式实现
name_with_b = [name for name in names if name[0] == 'B']

# lambda 函数和map函数联合使用 map(function, iter1) < map object >
print(map(lambda x: x ** 2, [i for i in range(6)]))
map_result = map(lambda x: x ** 2, [i for i in range(6)])
list_result = [x for x in map_result]

# lambda 函数和 map， filter函数联合使用 列表表达式 求取固定范围里偶数的平方
print(map(lambda x: x ** 2, filter(lambda y: y % 2 == 0, [z for z in range(10)])))
for i in map(lambda x: x ** 2, filter(lambda y: y % 2 == 0, [z for z in range(10)])):
    print(i)

# 需求: 求字符串每个单词的长度
stringWord = 'Hello this is python guide thanks for everything parents provides for us !'
print(stringWord.split(' '))
# < map object >
print(map(lambda word: len(word), stringWord.split(' ')))
word_length = map(lambda word: len(word), stringWord.split(' '))
# 列表推导式将其汇总出来
print([item for item in word_length])
# 可以调用enumerate函数将其顺序与其长度对应
print(enumerate([item for item in word_length]))
