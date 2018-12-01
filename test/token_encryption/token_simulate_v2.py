# -*-coding: utf-8-*-
"""
    这是一个关于微信开发公众号需要网页授权时，微信需要用户自己在授权url中带上一个类似token_status的参数，以防止跨域攻击
"""
__author__ = 'George'
__date__ = '2018/11/8'
__source_url__ = "https://blog.csdn.net/xc_zhou/article/details/80687825"

"""
    具体过程将在下面展示 按照流程进行展示
"""
# ***产生token ***
"""
    通过hmac sha1 算法产生用户给定的key和token的最大过期时间戳的一个消息摘要，将这个消息摘要和最大过期时间戳通过:凭借起来，再进行base64进行编码，生成token
"""
import time
import base64
import hmac
import os


def generate_token(key, expire=3600):
    """
    :param key: 用户给定的key，需要用户保存之后以便于验证token，每次产生token时可以是同一个key
    :param expire:最大有效时间
    :return: str token
    """
    # 生成key 摘要可以自己设定
    # key = base64.b64encode(os.urandom(24))
    # 将当前时间和过期时间字符串拼接 得到截至过期日期(时间戳格式)
    ts_str = str(time.time() + expire)
    # 将字符串格式的ts_str进行utf-8编码
    ts_byte = ts_str.encode("utf-8")
    # 将key 、ts_byte 通过固定方法生成新的字符串sha1
    sha1_tshexstr = hmac.new(key.encode("utf-8"), ts_byte, "sha1").hexdigest()
    # 拼接生成token
    token = ts_str + ":" + sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")


# ***验证token***
"""
    原理:将token进行base64进行解码(base64为对称加密),通过token得到最大过期时间戳和消息摘要，判断时间戳是否过期，如果没过期才将从token中取到的最大过期时间戳进行hmac sha1 算法运算(注意这里的key要与产生的token的key一致)，最后将产生的摘要与通过token取得的消息摘要进行对比，如果摘要一致，则token有效，否则token无效。
"""
import time
import base64
import hmac


# 模拟验证token
def certify_token(key, token):
    """

    :param key: str 用户给定的摘要
    :param token: str 从后台得到的token
    :return:  boolean
    """
    # 按照生成token的函数过程将token进行逆操作 得到token_str
    token_str = base64.urlsafe_b64decode(token).decode("utf-8")
    # 将得到的token进行切分操作 返回列表
    token_list = token_str.split(":")
    # 先判断长度 长度错误直接pass
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    # 截至之日的时间戳小于当前日期的时间戳 验证是否过期
    if float(ts_str) < time.time():
        # token expire
        return False
    # 进过长度检验 | 过期检验 得到发送请求时的ts_str 发送请求时的时间戳
    # 接下来只需要检验key摘要是否一致即可
    # 按照生成token 方法 再生成一次 检验是否一致 就可 ?? 不同的key是否会有相同过的value呢？？
    know_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"), ts_str.encode("utf-8"), "sha1")
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != know_sha1_tsstr:
        # token certification failed
        return False
    # token certification success
    return True

if __name__ == "__main__":
    # key 可以自己给定 也可以设置一个全局的key 相当于密钥之用
    key = "JD189DisjdkW8"
    # 生成token
    token = generate_token(key, 3600)
    # 验证token
    result = certify_token(key, token)
    print(result)