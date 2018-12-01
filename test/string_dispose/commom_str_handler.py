# -*-coding: utf-8-*-
"""
    计算机语言中对字符串的操作时必备的基础技能
"""
__author__ = "George"
__date__ = "2018/11/08"

# *** strip() ***
"""
    str.strip()就是把在这个字符串头和尾的空格，以及位于头尾的 \n \t 之类给删除掉
"""

string = '\t   hello \n tom jack\n '
print(len(string))
print(string.strip()) #
print(len(string.strip()))

# 对于\n 和 \t 有区别的
string_v1 = '\t   hello \t tom jack\n '
print(len(string_v1))
print(string_v1.strip())
print(len(string_v1.strip()))

# 实验证明: 只要在两头碰到了不存在strip()剥落方法中的元素，空格、\n、 \t 也算，那么那一头就会停止
string_v2 = 'hiahia hello, tom, ihih\t'
print(len(string_v2))
print(string_v2.strip("hia"))
print(len(string_v2.strip("hia")))
"""
    首先看str的头：第一个字母是h,包含在'hai'中，删掉。继续第二个字母是i包含在'hai'中，删掉。以此类推，一直到第一个空格，不包含在'hai'中。停止删除。
    再看str的尾巴：第一个字母是h，包含在'hai'中，删除。第二个字母i，包含在'hai'中，删除。以此类推，直到倒数第一个空格，停止删除。
至于中间到底有什么字母，都不管了。只要外围碰到不需要删除的字符，屠杀就结束了。
    字符串str还有另外两种类似的方法lstrip()和rstrip()。第一个是只删头，第二个是只删尾巴。用法类似。就不讲了。
"""
