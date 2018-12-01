# -*-coding:utf-8 -*-
# File :dict_test_p.py
# Author:George
# Date : 2018/11/24

"""
    字典是一个元素以键值对(key:value)形式呈现，以逗号分隔，以大括号包围得无序，可以修改得序列。
     无序 不支持索引
"""
# zip(itera1) 将几个序列对应为位得元素分别分到一个元祖当中 形成一个列表 资源组得个数取决为最短序列得长度
result = zip([1,2,3],('hello','george',18),('a', 'b','c', 'd'))
print(result) # <zip object at 0x000001B288769BC8>
for i in result:
    print(i)
# 字典构建
dict_test = {'a': 'hello', 'b': 'world'}
# 字典推导式  只能为统一value 默认为一个
keyList = ['name', 'age', 'password']
valueList = ['unknown']
man = {key:value for key in keyList for value in valueList }
print(man)

# 字典构建方法 dict(key=value)
george = dict(name='george', age=18, job='coder')
george_v1 = dict([("name",'george'),('age', 18),('job', 'coder')])
print(george)
print(george_v1)

# fromkeys(sequence) 创建字典 创建键值不等但是值相等得字典
print({}.fromkeys('abc',1))


# 字典常用操作方法
print(george.keys())
print(type(george.keys()))
# dict_key 可迭代对象
for i in george.keys():
    print(i)


# 获取字典中所有value
print(george.values())

print(george.items())
print(type(george.items()))
# dict_items 相当于列表嵌套元祖方式 可迭代对象
for i in george.items():
    print(i)

# get(key, default)  以键取值，如果键不存在，默认返回None 返回内容可以指定
print(george.get('name'))
# None 不存在返回None
print(george.get('dream'))


# setdefault() 设置默认值 不存在就添加新的Key
george.setdefault('dream', 'winner')
print(george.get('dream'))

# update 用字典来更新字典
dict_new = {'age':16, 'wife': 'miss'}
george.update(dict_new)
print(george.get('age'))
print(george.get('wife'))


# 移除pop(self, key)
george.pop('age')
print(george.get('age'))

# 移除后面一个
george.popitem()
print(george)

# clear() 清空字典
george.clear()
print(george)
