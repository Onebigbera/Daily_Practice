# -*-coding:utf-8 -*-
# File :number_conversion.py
# Author:George
# Date : 2018/11/23
"""
    使用python的内置函数实现多种进制之间的相互转换
    bin()  oct() int() hex()
"""
import os, sys

# base = [0, 1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']
base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]
print(base)


# 二进制到十进制 int(str, n=10)
def bin2dec(string_num):
    return str(int(string_num))


# 十六进制到十进制 int(str, n=16)
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


# 十进制到二进制 bin(str) bin()
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])
    return "".join([str(x) for x in mid[::-1]])

# 十进制到十六进制 cit()
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0:break
        num, rem = divmod(num, 16)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])

# 十进制到八进制
def dec2oct(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 8)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])


# 十六进制到二进制 hex2bin
def hex2bin(string_num):
    # 先将是十六进制数转化而十进制 在将十进制转化为二进制数
    return dec2bin(hex2dec(string_num.upper()))

# 二进制到十六进制 bin2hex
def bin2hex(string_num):
    # 二进制 -- 》 十进制 --》十六进制
    return dec2hex(bin2dec(string_num))


