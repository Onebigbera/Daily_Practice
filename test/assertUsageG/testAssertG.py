# -*-coding:utf-8 -*-
# File :testAssertG.py
# Author:George
# Date : 2018/12/31
"""
    assert 断言除了在 unittest 中有大量使用之外，python 中 assert的用法是怎么样的呢？
    python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发异常。
    如果断言正确，那么就会直接跳过，后面的参数就表示如果断言不正确时的错误原因
    assert 一般用法:
    assert expression [, argument]
    assert 表达式 [, 参数]
"""


def test_assertG():
    assert 1 == 1, " one is not equal to one"
    try:
        assert 2 * 3 == 2 + 3, '2*3 is not equal to 2+3'  # 此时抛出 AssertError异常 表达式和后面的参数是互逆的 表示如果断言不成立的原因
    except BaseException as msg:
        print(msg)


if __name__ == "__main__":
    test_assertG()
