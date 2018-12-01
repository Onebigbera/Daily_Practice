# -*- coding: utf-8 -*-
"""
    堆是具有以下性质的完全二叉树：
    每个分支节点的值都大于或者等于其左右孩子的值，称为大顶堆；
    每个分支节点的值都小于或者等于其左右孩子的值，称为小顶堆。
    因此，其根节点一定是所有节点中最大(小)的值。
    堆排序(heap sort) 就是利用大顶堆或者小顶堆的性质进行排序的方法。堆排序的总时间复杂度为O(nlogn)(下面采用大顶堆的方式)
    堆排序的运行时间主要消耗在初始构建堆和重建堆的反复筛选上。
其初始构建堆时间复杂度为O(n)。
正式排序时，重建堆的时间复杂度为O(nlogn)。
所以堆排序的总体时间复杂度为O(nlogn)。

堆排序对原始记录的排序状态不敏感，因此它无论最好、最坏和平均时间复杂度都是O(nlogn)。在性能上要好于冒泡、简单选择和直接插入算法。

空间复杂度上，只需要一个用于交换的暂存单元。但是由于记录的比较和交换是跳跃式的，因此，堆排序也是一种不稳定的排序方法。

此外，由于初始构建堆的比较次数较多，堆排序不适合序列个数较少的排序工作。
"""
__author__ = 'George'
__date__ = '2018/10/29'


class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用。"""
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def heap_sort(self):
        length = len(self.r)
        i = int(length / 2)
        # 将原始序列构造成一个大顶堆
        # 遍历从中间开始，到0结束，其实这些是堆的分支节点。
        while i >= 0:
            self.heap_adjust(i, length - 1)
            i -= 1
        # 逆序遍历整个序列，不断取出根节点的值，完成实际的排序。
        j = length - 1
        while j > 0:
            # 将当前根节点，也就是列表最开头，下标为0的值，交换到最后面j处
            self.swap(0, j)
            # 将发生变化的序列重新构造成大顶堆
            self.heap_adjust(0, j - 1)
            j -= 1

    def heap_adjust(self, s, m):
        """核心的大顶堆构造方法，维持序列的堆结构。"""
        lis = self.r
        temp = lis[s]
        i = 2 * s
        while i <= m:
            if i < m and lis[i] < lis[i + 1]:
                i += 1
            if temp >= lis[i]:
                break
            lis[s] = lis[i]
            s = i
            i *= 2
        lis[s] = temp

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret


if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.heap_sort()
    print(sqlist)
