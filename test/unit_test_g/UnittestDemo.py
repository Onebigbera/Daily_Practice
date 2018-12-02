# -*-coding:utf-8 -*-
# File :UnittestDemo.py
# Author:George
# Date : 2018/12/2
import os
import unittest


# 注意测试用例继承 unittest.TestCase
class TestStringMethod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        str = 'Hello world'
        self.assertEqual(str.split(), ['Hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            str.split(2)

print(os.getcwd())
if __name__ == '__main__':
    unittest.main()