# -*-coding:utf-8-*-
"""
    token:Token 的中文意思是'令牌'。主要是用来身份验证。Facebook, Twitter, Google+，Github等大型网站都在使用。比起传统的身份验证方法，Token具有扩展性强，安全性高等的特点，非常适合在web应用或者移动应用上使用。
"""
__author__ = 'George'
__date__ = '2018/11/8'
"""
    python中常见生成Token的方法
"""
# ******binascii.b2a_base64(os.urandom(24))[:-1]*****
"""
    这种算法的有点是性能快，缺点是有特殊字符，需要加replace做处理
"""
import binascii
import os

string_binascii = binascii.b2a_base64(os.urandom(24))[:-1]
print(string_binascii)

# *****sha1(os.urandom(24)).hexdigest()*****
"""
    这种算法的有点是安全，不需要做特殊处理。缺点是覆盖范围差一些。
"""
import hashlib
import os

string_hash = hashlib.sha1(os.urandom(24)).hexdigest()
print(string_hash)

# *****uuid4().hex*****
"""
    uuid 使用起来比较方便，抗重复性强，缺点就是安全性差一点
"""
import uuid

string_uuid = uuid.uuid4().hex
print(string_uuid)

# *****base64.b32encode(os.urandom(20))/base64.b64encode(os.urandom(24))
"""
    特别说明:可以用base64的地方，选择binascii.b2a_base64是不错的选择，更具W3的SessionID字符串的identifier的定义，SessionID中使用的base64，但是在Cookie的值内使用需要注意 "="这个特殊字符串的存在；
    如果要安全字符串(字母数字)，SHA1也是一个不错的选择，性能也不错。
"""
import base64
import os

string_base64_20 = base64.b32encode(os.urandom(20))
print(string_base64_20)
string_base64_24 = base64.b64encode(os.urandom(24))
print(string_base64_24)
