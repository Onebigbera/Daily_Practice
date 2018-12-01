# -*- coding:utf-8 -*-
"""
    回到装饰器的概念上来，装饰器接受一个callable对象，并返回一个callable对象，我们也可以用类来实现装饰器。让类的构造函数__init__()接受一个函数对象，然后重载其__call__方法并且返回一个函数，也可以达到装饰器的效果。
"""
__author__ = 'George'
__date__ = '2018/10/30'


# 不带参数的类装饰器
class Logging(object):
    def __init__(self, func):
        """

        :param func: 接受一个func对象
        """

        self.func = func

    def __call__(self, *args, **kwargs):
        """
        重载函数的__call__方法 返回函数执行对象
        :param args:
        :param kwargs:
        :return:
        """
        print(f'[DEBUG]:enter function "{self.func.__name__}"')
        return self.func(*args, **kwargs)


@Logging
def tell(something):
    print(f'tell tom {something}')


# 带参数的类装饰器
class LoggingParam(object):
    def __init__(self, level='INFO'):
        """
        如果需要通过类来实现带参数的类装饰器，那么在构造函数中接受的就不是一个函数对象而是传入的参数。通过类把这些参数保存起来，然后再重载__call__方法 接受一个函数并且返回一个函数。
        :param level: 传入的参数 默认等级为'INFO'
        """
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            """
            外部函数返回内部函数 传入函数变量
            :param args:
            :param kwargs:
            :return:
            """
            print(f'[{self.level}] enter function "{func.__name__}"')
            func(*args, **kwargs)

        return wrapper


@LoggingParam(level='INFO')
def say(something):
    print(f'tell the world {something}')


if __name__ == '__main__':
    # 不带参数的类装饰器
    tell(' i love him')

    # 被带参数的装饰器装饰
    say('life is beautiful')
