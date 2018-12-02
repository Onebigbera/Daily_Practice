# -*-coding:utf-8 -*-
# File :batch_model.py
# Author:George
# Date : 2018/12/2
"""
    每个py文件中放着不同功能的测试用例，方便维护，那么如何将他们一次性运行完呢，这里就需要用到unittest里面的defaultTestLoader.discover方法
"""
import unittest, HTMLTestRunner

# 实例化一个测试套件
suite = unittest.TestSuite()

# 知道指定目录下面的所有py文件
all_case = unittest.defaultTestLoader.discover(r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple',
                                               '*.py')

for case in all_case:
    # 循环添加case到测试集合中
    suite.addTest(case)

fw = open(r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple\test_report\batch_report.html', 'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fw, title='batch_files', description='batch files')

runner.run(suite)
