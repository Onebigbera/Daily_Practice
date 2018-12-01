# -*- coding: utf-8-*-
"""
    希尔排序时插入排序的改进版本，其核心思想时将原数据集合分割成若干个子序列，然后再对子学列分别进行插入排序，使子序列基本有序，最后再对全体进行一次直径二插入排序。
    这里最关键的是跳跃和分割的策略，也就是我们要怎么样分隔数据，间隔多大的问题。通常将相距某个'增量'的记录组成一个子序列，这样才能保证在子序列内分别进行直接插入排序后得到的结构是基本有序而不是局部有序，下面的例子是通过: increment = int(increment/3) + 1 来确定'增量'的值。
    希尔排序的时间复杂度为: O(n^3/2)
"""
__author__ = 'George'
__date__ = '2018/10/29'


class SQList(object):
    def __init__(self, list=None):
        """

        :param list:
        """
        self.list = list

    def shell_sort(self):
        """
        希尔排序
        :return:
        """
        list = self.list
        # 整个可迭代对象的长度
        length = len(list)
        # 设置默认增量
        increment = len(list)
        while increment > 1:
            increment = int(increment/3) + 1
            for i in range(increment + 1, length):
                if list[i] < list[i - increment]:
                    temp = list[i]
                    j = i - increment
                    while j > 0 and temp < list[j]:
                        list[j + increment] = list[j]
                        j -= increment
                    list[j + increment] = temp

    def __str__(self):
        list = []
        for i in self.list:
            list.append(i)
        return str(list)


if __name__ == '__main__':
    my_list = SQList([1,54,63,9,4,45,128,])
    my_list.shell_sort()
    print(my_list)


