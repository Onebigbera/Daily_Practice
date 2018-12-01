# -*-coding:utf-8 -*-
# File :mydict_test.py
# Author:George
# Date : 2018/11/26

import unittest
from unittest import TestCase

from test.unit_test_g.mydict import Dict


class TestDict(unittest.TestCase):

    def setUp(self):
        """
        比如测试需要连接数据库 此处设置连接数据库
        :return:
        """
        print('setUp...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def tearDown(self):
        # 此处设置关闭数据库
        print('tearDown...')

if __name__ == "__main__":
    unittest.main()

