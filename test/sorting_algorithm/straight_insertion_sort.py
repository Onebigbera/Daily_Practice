# -*- coding: utf-8 -*-
"""
    # TODO 多看几遍
    直接插入排序(straight insertion sort)
    基本思想就是将一个记录插入到已经排好序的有序表中，从而得到一个新的、记录数增加一的有序表。
    该算法需要记录一个辅助空间。最好情况下，当原始数据都是有序的情况下，只需要一轮对比，不需要移动记录，此时时间复杂度为O(N),然而，一般不可能如此。
    当最坏的情况，即待排序时逆序的情况下，比如[9,8,7,5,4,3] (n+2)(n-1)/2次，而记录的移动次数为(n+4)(n-1)/2次，如果排序记录是随机的，那么概率相等的原则，平均比较和移动次数大约为n^2/4次。因此我们得出直接插入算法的时间复杂度为O(n^2).同样的O(n^2)的时间复杂度，直接插入排序比冒泡排序和简单选择排序的性能要好。
"""
__author__ = 'George'
__date__ = '2018/10/29'


class SQList(object):
    def __init__(self, list=None):
        """

        :param list: 传入的iterator
        """
        self.list = list

    def insert_sort(self):
        list = self.list
        length = len(list)
        # 下标从1开始
        for i in range(1, length):
            if list[i] < list[i - 1]:
                temp = list[i]
                j = i - 1
                while list[j] > temp and j >= 0:
                    list[j + 1] = list[j]
                    j -= 1
                list[j+1] = temp


    def __str__(self):
        list = []
        for i in self.list:
            list.append(i)
        return str(list)


if __name__ == "__main__":
    my_list = SQList([1,54,78,9,16,48,84])
    my_list.insert_sort()
    print(my_list)
