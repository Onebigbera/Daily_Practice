# -*- coding:utf-8 -*-
"""
    首先说一下使用python模拟登录或注册时，对于带token的页面怎么登录注册模拟的思路：
    1、对于带token的页面，需要先从最开始的页面获取合法token
    2、然后使用获取到的合法token进行后续操作
    3.Token一般存储的地方有两个:
    一种是携带在Cookie中，一种是携带在response(页面返回的)隐藏表单中，获取方式类似
    注释:header是针对服务器有各种限制或者特定需求时使用的，一般服务器会进行类似的如: X-Requested-With、Content-Length、User-Agent等的验证，所以需要将其以字典形式发送给服务器。
    requests库是一个很重要、很强大的库

"""
__author__ = 'George'
__date__ = '2018/11/8'
__source_url__ = 'https://blog.csdn.net/foryouslgme/article/details/51822209'

"""
    此代码只是先了注册的第一步[手机发送验证码]，主要解决的获取Token具体操作有:获取页面第一次请求的重要信息，如: cookie 和 token
"""

import requests
# 模拟获取token
def register_token():
    # 拼接url
    host = "http://10.70.18.33:8083/"
    url1 = host + "shopxx-moble/register.jhtml"
    # 初始化url请求对象
    r = requests.get(url1)
    # 获取url请求对象中有用的信息,如 token、cookies
    token = r.cookies.items()[0][1]
    cookie = r.cookies
    # 以下为测试，所获取的token以及cookie的格式
    print(type(token))
    print(token)
    print(cookie)
    print(r.headers)
    print(r.url)
    # 手机号码发送验证码的url拼接
    url2 = host + "shopxx-mobile/register/send.jhtml"
    # 凭借header中的重要数据，如: token、cookie、User_Agent、Content_Length
    # 自己拼接创造一个header
    headers = {
        "token": token,
        "Host": "10.70.18.33:8083",
        "User-Agent": " Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
        "Content-Length": "18",
        "charset": "UTF-8",
        "cookie": "token=" + token
    }
    # 一般登陆注册页面均是post方法提交，需要将post需要提交的数据(此处为需要发送验证码的手机号码)进行组装拼接
    data = {"mobile": "1355451xxxx"}
    # 初始化post请求(需要传入url、提交的数据、header)
    s = requests.post(url2, data, headers=headers)
    # 打印返回结果
    print(s)
    print(s.status_code, s.text)

# 函数封装 如上:
if __name__ == '__main__':
    register_token()