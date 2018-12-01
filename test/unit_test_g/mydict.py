# -*-coding:utf-8 -*-
# File :mydict.py
# Author:George
# Date : 2018/11/26
"""
    编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问
"""
class Dict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object ha no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
