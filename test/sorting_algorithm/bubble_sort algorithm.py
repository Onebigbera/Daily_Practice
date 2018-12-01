# -*- coding:utf-8 -*-
# ************ First One**************
"""

    排序，就是将一串记录按照特定的规则(比如某些关键字的大小)递增或者递减排列起来的操作。
    排序的稳定性
        经过某种排序后，如果两个记录序号相等，且两者在源无序记录中先后顺序依然保持不变，则称所使用的排序方法是稳定的。
    内排序和外排序
        内排序: 排序过程中，待排序的所有记录全部放在内存中
        外排序: 排序过程中，使用到了外部存储
        通常讨论的都是内排序
    影响内排序算法性能的三个因素：
    时间复杂度:即时间性能，高效率的排序算法应该是具有尽可能少的关键字出现次数和记录的移动次数
    空间复杂度:主要是执行算法所需要的辅助孔吉纳，越少越好。
    算法复杂度:主要指代码的复杂度
    根据排序过程中借助的主要操作，可以把排序分为：
        插入排序
        交换排序
        选择排序
        归并排序
    按照算法复杂度可以分为两类:
        简单算法:包括冒泡排序、简单选择排序、直接插入排序
        改进算法:包括希尔排序、堆排序、归并排序和快速排序
    以下其中排序算法只是所有排序算法中最经典的几种，不代表全部。

"""
__author__ = 'George'
__date__ = '2018/10/29'

# 冒泡排序(Bubble sort)  时间复杂度O(n^2)
"""
    交换顺序的一种。核心思想是:两两比较相邻记录的关键字，如果反序则交换顺序，直到没有反序记录。
    其中实现细节不同，比如下面三种:
    1.最简单的排序实现: bubble_sort_simple
    2.冒泡排序: bubble_sort 
    3.改进的冒泡排序:bubble_sort_advance
"""


class SQList(object):
    def __init__(self, list=None):
        """

        :param list:
        """
        self.list = list

    def swap(self, i, j):
        """
        定义一个交换元素的方法，方便后面调用 护换索引对应的值
        :param i: list的索引
        :param j: list的索引
        :return:
        """
        temp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = temp
        # 为什么不行呢？
        # self.list[i], self.list[j] = self.list[j], self.list[j]

    def bubble_sort_simple(self):
        """
        最简单的交换顺序，时间复杂度为O(n^2) 从前面开始 每次将最小值送到最前面
        :return:
        """
        list = self.list
        length = len(self.list)
        for i in range(length):
            for j in range(i + 1, length):
                if list[i] > list[j]:
                    # 如果list[i]的值比list[j]大 交换位置 将较小值转移到前面
                    self.swap(i, j)

    def bubble_sort(self):
        """
        冒泡排序，时间复杂度O(n^2) 从后面开始 将最小的值送到最前面
        :return:
        """
        list = self.list
        length = len(list)
        for i in range(length):
            j = length - 2
            while j >= i:
                if list[j] > list[j + 1]:
                    self.swap(j, j + 1)
                j -= 1

    def bubble_sort_advance(self):
        """
        冒泡排序改进算法，时间复杂度为O(n^2)
        :return:
        """
        list = self.list
        length = len(list)
        # 立Flag 设置其初始值为True
        flag = True
        i = 0
        # todo:这个flag的作用在哪里呢？？？
        while i < length and flag:
            # 先变更flag
            flag = False
            j = length - 2
            while j >= i:
                if list[j] > list[j + 1]:
                    self.swap(j, j + 1)
                    # 解锁外部执行条件 只有当i=9时，不执行内部while语句，flag为False,外部while停止
                    flag = True
                # j的值向前推进一步
                j -= 1
                # i的值向后走一步
            i += 1

    def __str__(self):
        ret = []
        for i in self.list:
            ret.append(i)
        return str(ret)


if __name__ == '__main__':
    sqlist = SQList([6, 5, 47, 89, 78, 45, 1, 45, 4])
    # sqlist.bubble_sort_simple()
    # sqlist.bubble_sort()
    sqlist.bubble_sort_advance()
    print(sqlist)
