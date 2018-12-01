# -*-coding:utf-8 -*-
# File :math_module.py
# Author:George
# Date : 2018/11/24

"""
    math模块是一个重要的计算模块
"""
import math

# 常数e 2.718...
print(math.e)

# 常数pi 圆周率 3.14159...
print(math.pi)

# 指数次方   x**y
print(math.pow(3, 5))

# 返回不小于x的整数 6
print(math.ceil(5.4))

# 返回x的整数部分 4
print(math.trunc(5.4))

# 返回不大于x的最大整数
print(math.floor(5.4))

# 返回x的绝对值
print(math.fabs(-4.5))

#返回x%y  取余数
print(math.fmod(5, 2))

# 对迭代器中每个元素进行迭代求和 返回无损精度的和
print(math.fsum([x for x in range(10)]))

# 返回x的阶乘  x! x*(x-1)(x-2)...1
print(math.factorial(5))

# 返回以x和y为直角边的斜边长
print(math.hypot(3, 4))

# 将度数化为弧度
print(math.radians(30))

# 返回x(弧度)的三角正余弦
print(math.sin(math.radians(30)))

# 返回x的反三角正余弦
print(math.asin(0.5))

# 返回x的三角余弦值
print(math.radians(45))