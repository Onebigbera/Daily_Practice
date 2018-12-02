# -*-coding:utf-8 -*-
# File :parameterization.py
# Author:George
# Date : 2018/12/2

"""
    测试一般都是调用维护文档就可以 用文件作为参数对unittest进行单元测试
# """
import unittest, HTMLTestRunner
from parameterized import parameterized


# 自定义一个Cvs文件读取函数
def redCvs(path, sep=','):
    list = []
    # rb 二进制读取 兼容性好 文档流操作
    with open(path, 'rb') as f:
        for line in f:
            # 二进制是encoded 被编码的 所以需要解码 去除两边空格 按照','切分
            list1 = line.decode().strip().split(sep)
            list.append(list1)
        print(list)
        return list


# redCvs(r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple\a.txt')


def login(username, password):
    if username == 'george' and password == 123456:
        return True
    return False


class Login_G(unittest.TestCase):

    @parameterized.expand(redCvs(r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple\a.txt'))
    # exception 机制
    def testta(self, username, password, exception):
        result = login(username, password)
        self.assertEqual(exception, result)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Login_G))
    fw = open(r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple\test_report\param_2.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fw, title='parameterization', description='why')

    runner.run(suite)
