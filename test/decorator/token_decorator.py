# -*- coding:utf-8 -*-
"""
    根据需求的不断提升和更改，逐渐完善装饰器的功能

"""
__author__ = 'George'
__date__ = '2018/11/7'
__source_url__ = 'http://blog.51cto.com/alsww/1717521'
from functools import wraps


# 需求:要求在函数运行前和运行后打印函数名称
def auth_test(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        print(f'Before {func.__name__}')
        result = func(*args, **kwargs)
        print(f'After {func.__name__}')
        return result

    return _wrapper


@auth_test
def tell(name):
    print(f'hello, my name is {name}')


# tell('tom')
"""
    需求:要求判断用户是否登陆成功的功能 只有在登陆成功前提下才能进行相关操作
"""


# 此处的login函数对象肯定是一个可以调用的对象 为了测试这里的login函数必定返回真
def login():
    name = 'tom'
    password = '123456'
    if name == 'tom' and password == '123456':
        return True
    else:
        return False


def auth_login(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        print(f'Before {func.__name__}')
        login_status = login()
        if not login_status:
            return 'Illegal user'
        result = func(*args, **kwargs)
        print(f'After {func.__name__}')
        return result

    return _wrapper


@auth_login
def play(name):
    print(f'today i play with {name}')


# play('Tomcat')

"""
    检验是否携带正确的token  v1
"""


# 可调用函数login_token检验token中的key
def login_token(key):
    local_key = 'AUTHENTICATE_VOCABULARY'
    if local_key == key:
        return True
    else:
        return False


def auth_login_token_flag(flag=True):
    def auth_login_token(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            # 前面讲到过单独用kwargs时  其就是一个字典 解包功能
            print(f' Before {func.__name__}')
            # 如果flag为True
            if flag:
                # 建立token和key的映射关系 解包后为一个字典 | 解包很关键
                key_token = kwargs['token']
                # 删除 token的值
                # del kwargs['token']
                # key_token = kwargs.pop('token')
                # 带入login_token函数中
                is_login = login_token(key_token)
                if not is_login:
                    print(f'Illegal User exit soon key error !')
                    return 'Illegal User'
                result = func(*args, **kwargs)
                print(f' After {func.__name__}')
                return result
            # flag 为False时 免检
            print(f'need not auth_key')
            result = func(*args, **kwargs)
            return result

        return _wrapper

    return auth_login_token


login_token('hello_world')


# 注意装饰器对象用哪一个
@auth_login_token_flag(flag=True)
# 执行函数 默认token为 None
def jump(name, token=None):
    token = 'AUTHENTICATE_VOCABULARY'
    print(f' {name} could jump a long distance')


# 在token为正切的情况下 函数才能正常运行
jump('george', token='AUTHENTICATE_VOCABULARY')

"""
    V2
"""

# 模拟数据源 用户信息列表 进行判断 | 相当于数据库
user_list = [
    {'name': 'jack', 'password': '123'},
    {'name': 'jordan', 'password': '123'},
    {'name': 'mike', 'password': '123'},
]
# 记录当前用户状态(是否登陆|登陆是否成功)的字典！
current_user = {'name': None, 'login': False}


# 第一层里面可以传入的参数是一些指标参数:flag level type等
def auth_test_one(auth_type='field'):
    def auth_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 打印认证的类型
            print(f'auth_type:{auth_type}')
            if auth_type == 'field':
                # 如果用户名称存在于数据库中且用户已经登陆 | 用户已经是登陆状态
                if current_user['name'] and current_user['login']:
                    result = func(*args, **kwargs)
                    return result
                # 如果不同时满足用户名称存在和登陆状态为True
                name = input('请输入用户名:').strip()
                password = input('请输入密码:').strip()
                for user_dict in user_list:
                    # 验证输入用户名称和密码是否存在于数据库 | 存储数据的地方
                    if name == user_dict['name'] and password == user_dict['password']:
                        # 登陆成功 更改记录状态的字典| 记录当前的name 和 登陆状态 主要是name
                        current_user['name'] = name
                        current_user['login'] = True
                        # 验证成功
                        result = func(*args, **kwargs)
                        # 回调函数
                        return result
                    else:
                        print(f'账户密码错误，请重新输入！')
            # 自定义免检类型 | 自定义级别完善
            elif auth_type == 'root':
                print(f'认证类型为:{auth_type}')
                result = func(*args, **kwargs)
                return result

        return wrapper

    return auth_func


"""
    在调试时记得用一致的名称 但是不一致也没错 需要继续去改进
"""


# 模拟第一次输入账户密码
@auth_test_one(auth_type='field')
def home(name):
    print(f'欢迎回来,{name}')


# home('tom')
# 将当前的用户状态字典打印出来方便调试
print(current_user)


# 模拟第二次带token直接登陆 不用再次输入
@auth_test_one(auth_type='field')
def shopping_car(name):
    print(f'{name} 的购物车里有:一本书、一颗糖')

# shopping_car('tom')
