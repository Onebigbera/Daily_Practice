# -*-coding:utf-8 -*-
# File :unittest_model_g.py
# Author:George
# Date : 2018/12/2

"""
    HTMLTestRunner是生成html报告的模块 方便自己查看结果 xml生成的报告是以后给jekens工具使用 能自动识别测试报告内容
"""
import unittest
import xmlrunner
import HTMLTestRunner


class MyTest(unittest.TestCase):
    # 测试用例必须以test开头 不然不会识别
    def testa(self):
        # 描述 会同测试用例标题一并显示在测试报告中
        """a"""
        # 进行断言
        self.assertEqual(1, 1)

    def testhaha(self):
        """b"""

        self.assertEqual(2, 1)

    def testb(self):
        """hello"""
        self.assertEqual(3, 2)


# 另外一个测试用例
class MyTest2(unittest.TestCase):
    def testc(self):
        '''d'''
        self.assertEqual(1, 1)


    def testhaha(self):
        '''e'''
        self.assertEqual(2, 1)

    def testd(self):
        '''f'''
        self.assertEqual(3, 2)


if __name__ == "__main__":

    # 运行测试用例的类
    #unittest.main()
    # 定义一个测试套件
    suite = unittest.TestSuite()

    # 添加测试用例方法一 向测试套件中添加测试用例
    # suite.addTest(MyTest('testa'))
    # suite.addTest(MyTest('testb'))

    # 添加测试用例二 向测试套件中添加测试类的所有测试用例
    suite.addTest(unittest.makeSuite(MyTest))

    # 定义一个文件对象 给后面的HTMLTestRunner生成测试报告用 注意打开方式必须为 wb
    # 路径问题由于 \t 是制表符  \n 是换行符  直接用 r''源生就可以
    fw = open(r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple\test_report\unitTest.html', 'wb')

    # 生成测试报告方法一
    runner = HTMLTestRunner.HTMLTestRunner(stream=fw, title='Testing', description='description')

    # 生成测试报告方法二 这种方式只需要指定生成测试报告的目录就可以
    # runner = xmlrunner.XMLTestRunner(output=r'F:\Python_guide\Daily_Practice\test\unit_test_g\unittest_simple\test_report')
    runner.run(suite)

"""
    生成测试报告如果在pycharm IDE中无法生成 那就将.py文件当作脚本在cmd中运行
    
"""