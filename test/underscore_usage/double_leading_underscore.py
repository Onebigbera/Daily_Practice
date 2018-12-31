# -*-coding:utf-8 -*-
# File :double_leading_underscore.py
# Author:George
# Date : 2018/12/29
"""
    The usage of double leading underscore
"""


class TestG(object):

    def __init__(self):
        self.foo = 11
        self._bar = 25
        self.__baz = 45

    # 保护属性 防止被更改
    def __say(self):
        print("Hello Python")

    def use__say(self):
        self.__say()


class ExtendTest(TestG):
    def __init__(self):
        super().__init__()
        self.foo = "overridden"
        self._bar = "overridden"
        self.__baz = "overridden"

    def __talk(self):
        print("Hello world!")

    def use__talk(self):
        self.__talk()

_MangledGlobal__mangled = 32

class MangledGlobal(object):
    """

    """
    def test2(self):
        """

        :return:
        """
        # it is really surprised me
        return __mangled

result = MangledGlobal().test2()

if __name__ == "__main__":
    test = TestG()
    print(dir(test))

    test1 = ExtendTest()
    print(test1.foo)
    print(test._bar)
    print(dir(test1))
    print(test1._ExtendTest__baz) # 重写的方法           overridden
    print(test1._TestG__baz)       # 原来的方法依旧保留   45
    # print(test1.__baz)    # "ExtendTest " object has no attribute __baz
    # print(test1.__talk())
    print(dir(ExtendTest))
    test1.use__talk()
    test1.use__say()
    # test1.__say()
    print(result)           # 32


