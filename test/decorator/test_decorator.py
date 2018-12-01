"""
装饰器: python 装饰器主要时为了在被装饰函数的基础上进行功能扩展，实现逻辑上的切面编程 引入Java中面向切面编程思想（Aspect_Oriented Programming ）
不改变函数代码前提下动态添加函数功能
装饰器装饰过的函数看上去名字没变，其实已经变了。为什么会这样呢？只要你想想装饰器的语法糖@代替的东西就明白了。@等同于这样的写法:test_decorator = TestDecorator(test_decorator) 而外层函数返回的是__wrapper_inner,那么test_decorator的__name__自然就变为__wrapper_inner了，不仅仅是name,其他属性例如：doc、source等全都变为__wrapper_inner的了 用 functools包里面的wraps可以基本解决这个问题。@wraps装饰器
    虽然能解决主要问题，但是还不太完美，因为函数的签名和源码还是拿不到。要彻底解决这个问题的依赖第三方包 wrapt

"""

from functools import wraps


# 装饰器类和__call__ 最简单的装饰器类
class TestDecorator(object):
    def __init__(self, func):
        """

        :param func: 其装饰的函数对象  函数对象 很多地方调用过
        """
        self.func = func

    # 调用函数   调用时返回执行函数
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


# 该装饰器功能 动态添加func函数功能
@TestDecorator
def foo(x, y):
    return x ** y


# 定义一个最简单的计时器的类
def wrapper_time(func):
    """
    不带参数的装饰器
    :param func: 被装饰的函数
    :return: 返回值
    """

    # 使之正常返回
    @wraps(func)
    def __wrapper_inner(*args, **kwargs):
        """
        使用装饰器@wraps是让使用__doc__函数时能够看到内部函数的说明文档（docstring）
        :param args: tuple_type arguments
        :param kwargs: dict_type arguments
        :return:
        """
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        # 返回包含小数点后5为的浮点型数据 %.5f(小数点后保留5位的浮点数)
        process_time = '%.5f' % (end_time - start_time)
        # .__name__ 魔术方法 打印对象名称
        print(f'函数{func.__name__} 运行花费的时间为:{process_time}')
        return result

    return __wrapper_inner


@wrapper_time
def test_decorator(name):
    import time
    time.sleep(3)
    print(f'the func has sleep with {name} for 3 seconds')


# test_decorator('Tomcat')


# 带参数的时间装饰器函数 将参数带进去
def wrapper_time_param(flag=None):
    """
    :param flag: 决定是否计时的条件关键字
    :return:
    """

    # 再套取一层 用来判断
    def wrapper_time(func):
        """
        不带参数的装饰器
        :param func: 被装饰的函数
        :return: 返回值
        """

        @wraps(func)
        def __wrapper_inner(*args, **kwargs):
            """
            使用装饰器@wraps是让使用__doc__函数时能够看到内部函数的说明文档（docstring）
            :param args: tuple_type arguments
            :param kwargs: dict_type arguments
            :return:
            """
            print('装饰器里层被调用')
            # 是否需要计时的触发器(关键字决定)  先添加一层判断
            if not flag:
                print('不用统计计时时间')
                # return 不用统计时间之间运行func函数 return是函数结束标志 这里return 返回一个值后就不会执行下面代码
                return func(*args, **kwargs)
            # flag为true时
            import time
            start_time = time.time()
            # 运行func 函数
            result = func(*args, **kwargs)
            end_time = time.time()
            # 返回包含小数点后5为的浮点型数据 %.5f(小数点后保留5位的浮点数)
            process_time = '%.6f' % (end_time - start_time)
            # .__name__ 魔术方法 打印对象名称 将运行时间打印出来
            print(f'函数{func.__name__} 运行花费的时间为:{process_time}')
            return result

        return __wrapper_inner

    return wrapper_time


@wrapper_time_param(True)
def count_decorator(number):
    sum = 0
    import time
    time.sleep(4)
    print(f'the func has sleep for 4 second ')
    for i in range(number):
        sum += i
    print(sum)
    return sum


count_decorator(20000000)
