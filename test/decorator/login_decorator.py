# -*- coding:utf-8 -*-
"""
    One man can be destroyed but not brought down
    Create a decorator to judge whether uer is login
    需要导入Django模块中的HttpResponseRedirect
"""
__author__ = "George"
__data__ = "2018/11/15"

# 当用户未登陆时 需要用到重定向跳转到登陆界面
from django import HttpResponseRedirect
from functools import wraps


def test_wrapper(flag=True):
    # 外层函数返回内层函数对象
    def test_login(func):
        # 内层函数
        @wraps(func)
        def is_login(request, *args, **kwargs):
            # 先检验flag
            if flag:
                return func(request, *args, **kwargs)
            # 从request请求中判断是否存在用户id
            if request.sesssion.get("user_id"):
                # 存在则返执行函数
                return func(request, *args, **kwargs)
            else:
                # 不能从request中取到用户id 则调用重定向
                redirect = HttpResponseRedirect("/user/login")
                # 在重定向页面中设置cookie
                redirect.set_cookie("url", request.get_full_path)
            # 返回重定向页面
            return redirect

        return is_login

    return test_login
