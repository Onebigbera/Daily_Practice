# -*-coding:utf-8 -*-
# File :test_Unicode_bytes_bytearray.py
# Author:George
# Date : 2019/1/3
# motto: Someone always give up while someone always try!

#     Python字符串使用Unicode编码来表示文本,大致而言，每个Unicode字符都用一个码点（code point）表示，而
# 码点是Unicode标准给每个字符指定的数字。这让你能够以任何现
# 代软件都能识别的方式表示129个文字系统中的12万个以上的字
# 符。当然，鉴于计算机键盘不可能包含几十万个键，因此有一种指
# 定Unicode字符的通用机制：使用16或32位的十六进制字面量（分
# 别加上前缀\u或\U）或者使用字符的Unicode名称（\N{name}）。
# 详情参考 http://unicode-table.com
"""
    教材上演示代码
"""
import math

print("\u00C6")
# print("\U0001F60A")
cat = "This is a cat:\N{cat}"
print(cat)
print("\U0001F60A")
"""
    使用 ASCLL 、UTF-8、UTF-32编码将字符串转换为bytes    
"""
"""
    为了实现多文字符号的实现和内存的浪费，Python中使用可变长度编码来编码字符即对于不同的字符，使用不同数量的字节进行编码。这种
编码方式主要出自计算机先锋Kenneth Thompson之手。通过使用这
种编码，可节省占用的空间，就像摩尔斯码使用较少的点和短线表
示常见的字母，从而减少工作量一样 。具体地说，进行单字节编
码时，依然使用ASCII编码，以便与较旧的系统兼容；但对于不在
这个范围内的字符，使用多个字节（最多为6个）进行编码。下面
来使用ASCII、UTF-8和UTF-32编码将字符串转换为bytes。

"""
str = "Hello, world!"
print(str.encode("ASCII"))
print(str.encode("UTF-8"))
print(str.encode("UTF-32"))

# 比较相同字符串经过编码方式编码后的长度对比
str = "How long is this?"
print(len(str.encode("UTF-8"))) # 17
print(len(str.encode("UTF-32")))    # 72

"""
    可不使用方法encode和decode，而直接创建bytes和str（即字符
串）对象，如下所示：
"""
# string = bytes(("Hællå, wørld!", encoding='utf-8')
# string =  str(b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!', encoding="utf-8")

"""
    Python还提供了bytearray，它是bytes的可变版。从某种
意义上说，它就像是可修改的字符串——常规字符串是不能修改
的。然而，bytearray其实是为在幕后使用而设计的，因此作为类
字符串使用时对用户并不友好。例如，要替换其中的字符，必须将
其指定为0～255的值。因此，要插入字符，必须使用ord获取其序
数值（ordinal value）
"""
x = bytearray(b"Hello!")
x[1] = ord(b"u")
print(x)
print(abs(-43))
print(float(454.34))

"""
    四舍五入
    int() 获取数字的整数部分
    math.floor() 获取数字的整数部分(不大于该数的整数)
    math.ceil() 获取不小于该数的整数
    round() 四舍五入 当小数位5时 取偶数
"""

print(int(3.1))
print(int(3.9))

print(math.floor(3.1))
print(math.floor(3.9))

print(math.ceil(3.1))
print(math.ceil(3.9))

print(round(3.1))
print(round(3.5))
print(round(3.9))