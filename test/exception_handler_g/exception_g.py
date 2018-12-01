# -*-coding:utf-8 -*-
# File :exception_g.py
# Author:George
# Date : 2018/11/25
"""
    运行系统项目时 系统会报BUG是不可避免地 如何正确地DEBUG是作为一名合格程序员的必备技能 但是 DEBUG的前提是了解BUG所在地 当系统中有暂时不能处理的BUG 却不能影响整个项目的进度时 此时的try...except模块就能发挥大的作用
"""


# 需求: 在系统抛出bug时 我们希望程序能正常执行下去而不是停止
def test_exception(par1, par2):
    try:
        result = par1 / par2
    except ZeroDivisionError as e:
        print(e)
    else:
        return 'result is {}'.format(result)


# test_exception(3, 0)
# print(test_exception(12, 3))

# except 后面不接任何错误类型
def test_exceptionG(par1):
    try:
        result = filter(lambda x: x ** 2, par1)
    # except也不可不接任何bug类型 直接进入解决语句 不负责任的表现
    # except:
    # 直接接Exception 将错误类型打印出来
    # except Exception as e:
    # python 中的错误都是类class 所有的错误都集成BaseException 捕获了BaseException 会在捕获错误的同时也捕获他的子类
    except BaseException as e:
        print(e)
        print('程序错误, DEBUG')
    else:
        print(result)
        return result
    finally:
        # finally 函数是函数调用一定会执行的部分 就算return函数返回了结果
        print('Hello python')


# test_exceptionG([1, 2, 3])


# test_exceptionG(113)


# 当程序出现错误太多时 不使用错误码 直接用except带多种异常也可以
def test_var_error(par1, par2):
    try:
        result = 5 / par1 + sum(filter(lambda x: x % 2 == 1, par2))
    except(ZeroDivisionError, TypeError):
        print('出现了 ZeroDivisionRrror 或者 TypeError')


# test_var_error(0, 32)


''' 跨越多层级调用
'''


def foo1(num):
    return 2 / num


def foo2(num):
    return foo1(num=num)


def main_g(num):
    return foo2(num=num)


def operation_g():
    try:
        main_g(0)
    except Exception as e:
        print(e)
        print('DEBUG')
    else:
        print(main_g(0))
    finally:
        print('Nice world！')


# 多层包装的情况下 只要捕获到错误就可以处理
operation_g()
