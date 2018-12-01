# -*-coding: utf-8-*-
"""
    检验用户是否登陆(用户模块|购物车模块...)在很多模块中都会用到，为了给对应函数动态添加这一功能，用户登陆状态装饰器是一个非常普遍也是非常重要的装饰器。
"""
from functools import wraps

__author__ = 'George'
__date__ = '2018/11/7'
__annotation__ = 'copied from decorators.py   Incomplete'

REDIRECT_FIELD_NAME = 'next'


def user_passes_test_test(test_func, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorators for view that check that the user passes the given test,redirecting to the log-in page if necessary. The test should be a callable that takes the user object and return True id the user passes.
    :param test_func:
    :param login_url:
    :param redirect_field_name:
    :return:
    """

    # 外层函数并没有返回内层函数而是返回自身？？？？？？？？？？？？
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            resolved_login_url = resolved_url(login_url or settings.LOGIN_URL)
            # If the login url is the same scheme and net location then just
            # use the path as the 'next' url
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not login_scheme or login_scheme == current_shceme) and (
                    not login_netloc or not login_netloc == current_netloc)):
                path = request.get_full_path()
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(path, resolved_login_url, redirect_field_name)

        return _wrapped_view

    return decorator


# django框架中的login_required装饰器
def login_required_test(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in ,redirecting to the login-in page if necessary  _copied
    :param function:
    :param redirect_field_name:
    :param login_url:
    :return:
    """
    actual_decorator = user_passes_test(
        # lambda 函数检验用户是否验证 True|False
        lambda u: u.is_authenticated,
        # 登陆的url
        login_url=login_url,
        # 重定向名称
        redirect_field_name=redirect_field_name
    )
    # 如果函数存在
    if function:
        # 将函数代入
        return actual_decorator(function)
    # 如果函数不存在 直接返回actual_decorator函数对象
    return actual_decorator
