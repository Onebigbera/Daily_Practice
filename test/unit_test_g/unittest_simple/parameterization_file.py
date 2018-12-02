# -*-coding:utf-8 -*-
# File :parameterlization_file.py
# Author:George
# Date : 2018/12/2

"""
    参数化一般分两种情况: 一种是需要大量数据还有一种是有唯一性校验的情况下都需要参数化那么在unittest中是如何实现的呢
"""
import unittest, HTMLTestRunner
# 自己扩展的
from parameterized import parameterized


def login(username, password):
    if username == 'george' and password == '123456':
        return True
    else:
        return False


class LoginG(unittest.TestCase):

    @parameterized.expand([
        # 可以是列表 也可以是元祖
        ['george', '123456', True],
        [' ', '123456', True],
        ['steven', '', False],
        ['hello', '123456', False]
    ]
    )
    # 这里面的参数对应上面二维列表中的参数，系统会遍历元素 直至调用遍历完成
    def test_login(self, username, password, exception):
        """登陆"""
        result = login(username, password)
        self.assertEqual(result, exception)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LoginG))
    fw = open(r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple\test_report\param.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fw, title='parameterization', description='how')
    runner.run(suite)
