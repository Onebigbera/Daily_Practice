# -*-coding: utf-8-*-
"""
    函数作用域是函数中的基础问题，也是函数变量执行空间的优先级准则。
"""
__author__ = "George"
__date__ = "2018/10/09"

"""
    下面从一个闭包函数来分析常见的函数作用域
"""

file_name = "function_scope.py"
def wrapper():
    filename = "enclosed.py"

    def show_filename():
        return "filename : % s" % filename

    # 输出filename
    print(filename)
    return show_filename


wrapper()