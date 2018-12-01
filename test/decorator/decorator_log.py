# -*- coding:utf-8-*-
"""
    @就是一种语法糖 装饰器&语法糖(syntax sugar)
    装饰器执行流程可以类比于将针贯穿一颗洋葱
    带参数的解释器和类装饰器属于进阶的内容。在理解这些装饰器之前，最好对函数的闭包和装饰器的接口API约定由一定的了解。
    假设我们需要一个打出函数的运行信息并且打出log信息的等级，则装饰器如下:
"""
from functools import wraps
__author__ = 'George'
__date__ = '2018/10/31'

"""
    设定函数的调试等级和函数名打印出来 方便DEBUG
"""
# 简单些一个能打印日志等级的装饰器
# 放装饰器参数 装饰器变量层
def logging(level):
    # 函数对象
    def wrapper(func):
        # 函数参数层
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            print(f'{level}:enter function "{func.__name__}"')
            return func(*args, **kwargs)

        return inner_wrapper

    return wrapper


@logging(level='INFO')
def say(something):
    print(f'say {something}')

# 如果么有使用@语法糖，等同于
# say = logging(level='INFO')(say)

@logging(level='INFO')
def do(something):
    print(f'do {something}')


if __name__ == '__main__':
    say('i love python')
    do('love word')