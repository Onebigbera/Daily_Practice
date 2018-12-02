# -*-coding:utf-8 -*-
# File :setup_teardown_usage.py
# Author:George
# Date : 2018/12/2

"""
    setUp 和 tearDown的运用
"""
import unittest

import HTMLTestRunner
import xmlrunner


class TestUsage(unittest.TestCase):

    @classmethod
    # 类开始运行前 比如在执行这些实例之前需要备份数据库等操作
    def setUpClass(cls):
        print('Before class operation perform')

    @classmethod
    # 类结束运行后 比如在执行完这些类后需要还原数据库
    def tearDownClass(cls):
        print('After class operation perform ')

    # 测试用例执行前
    def setUp(self):
        string = 'before'
        print('----这是在测试用例执行前----')

    # 测试用例执行后
    def tearDown(self):
        string = 'after'
        print('----测试用例执行后----')

    def testProcess(self):
        print('----测试执行1---')
        self.assertEqual(1, 1)

    def testProcess2(self):
        print('---测试用例2----')
        self.assertEqual(1, 2)

if __name__ == "__main__":
    # 第一步  实例化suite套件
    suite = unittest.TestSuite()

    # 第二步 向实例化的套件中添加类或者方法
    suite.addTest(unittest.makeSuite(TestUsage))
    # 添加单独方法用例
    # suite.addTest(TestUsage('testprocess'))

    # 第三步 生成xml或者html打印装置
    fw = open(r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple\test_report\setUp_tearDown_usage.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fw, title='usage_setUp_tearDown', description='how it work')

    # 生成xml runner
    # runner = xmlrunner.XMLTestRunner(output=r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple\test_report')

    # 第四步  运行xmlrunner
    runner.run(suite)

    # 第五步  在cmd中执行