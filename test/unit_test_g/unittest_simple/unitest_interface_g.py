# -*-coding:utf-8 -*-
# File :unitest_interface_g.py
# Author:George
# Date : 2018/12/2

"""
    基本不存在单独的接口 一般都是依赖接口 比如购买商品:依赖登陆接口中session或者token 这些都是变化的  那么在unittest中如何实现的呢？
"""
import unittest, HTMLTestRunner

import xmlrunner


def login(username, password):
    if username == 'george' and password == '123456':
        return '9527'
    return False


def shopping(sign):
    if sign == '9527':
        return True
    return False


class MyShopping(unittest.TestCase):
    # 这里不以test开头命名 就是一个普通方法 在执行测试用例的时候并不会执行 在调用的时候才会执行
    def login(self):
        res = login('george', '123456')
        return res

    def test_login_cj(self):
        result = self.login()
        self.out = shopping(result)
        self.assertEqual(self.out, True)
if __name__ == "__main__":
    # 实例化测试套件
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MyShopping))
    # fw = open(r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple\test_report\shop.html', 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fw, title='associated_interface', description='shopping_test')

    runner = xmlrunner.XMLTestRunner(output=r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple\test_report')
    runner.run(suite)