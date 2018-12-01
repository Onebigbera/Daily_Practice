# -*- coding: utf-8-*-
# ****************Second One ****************
"""
    简单选择排序(simple_selection_sort) 时间复杂度O(N^2)
    通过n-1次关键字之间的比较，从n-i+1个记录中选出关键字最小的记录，并和第i(1<=i<=n)个元素护换位置
    通俗的说，对尚未完成排序的所有元素，从头到尾比较一边，记录下来最小的那个元素的下标，也就是该元素的位置，再把该元素教化到当前遍历的最前面，其效率住处在于:每一轮进行了很多的比较，却只交换一次。因为它的时间复杂度也是O(n^2)但还是要比冒泡排序要好一点。
"""
__author__ = 'George'
__date__ = '2018/10/29'


class SQList(object):
    def __init__(self, list=None):
        """

        :param list: 传入的可迭代对象
        """
        self.list = list

    def swap(self, i, j):
        """
        定义一个交换元素的方法，方便在之后使用 依据索引交换位置
        :param i:
        :param j:
        :return:
        """
        temp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = temp

    def select_sort(self):
        """
        简单的选择排序，时间复杂度为O(n^2)

        :return:
        """
        list = self.list
        length = len(list)
        for i in range(length):
            # 默认最小值的索引为i
            minimum = i
            for j in range(i + 1, length):
                if list[minimum] > list[j]:
                    # 如果后面有更小的 定位最小值得索引
                    minimum = j

            # 如果最小值得位置不是i
            if i != minimum:
                # 将最小值位置和当前遍历元素护换位置
                self.swap(i, minimum)

    def __str__(self):
        list = []
        for i in self.list:
            list.append(i)
        return str(list)


if __name__ == '__main__':
    my_list = SQList([1, 78, 98, 7, 15, 56, 23])
    my_list.select_sort()
    print(my_list)