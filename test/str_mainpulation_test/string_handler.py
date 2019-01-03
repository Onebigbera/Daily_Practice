# -*-coding:utf-8 -*-
# File :string_handler.py
# Author:George
# Date : 2018/11/24
"""
    string dispose
"""

"""
     sting[start:end:step] 切片操作
"""
string_test = 'manipulation'

# print(string_test[2:3])

# 返回None
# print(string_test[2:3:-1])

# 倒转字符串 notalupinam
# print(string_test[::-1])

# noitalupinam 倒换字符串
# print(string_test[-1::-1])

# 从索引值为-2开始取 on
# print(string_test[-2::])

# 从索引值为-1开始取 正向取值 n
# print(string_test[-1::])

# 当步长为-值时 [A:B:-1] A的默认值为-1 从右边开始取值
# no
print(string_test[:-3:-1])
# no
print(string_test[-1:-3:-1])
# None
print(string_test[0:-3:-1])

# 验证 None
print(string_test[-4:-2:-1])

# repr 和 str 用法的区别
print(repr("Hello \n world"))    # 'Hello \n world'
print(str("Hello \nworld "))    # 会识别出字符串中的 \n 换行符从而换行
print("Hello world")

print(r"Let's go!")    # 当单引号和双引号没有冲突时，r源生方法表示源生
print(r'Let\'s go!') # 但字符串中出现 '单引号时明系统还是不能判别停止位置，从而需要转义 结论: \ 转义字符可以在 r原始字符串中生效

# 原始字符串不能以单个反斜杠结尾
# print(r"This is illegal\")      # SyntaxError: EOL while scanning string literal
print(r"This is illegal\\")
# 指定原始字符串，可以用单引号或者双引号将其括起来，还可以将其使用三引号括起来。
