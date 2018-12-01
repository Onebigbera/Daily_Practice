# -*- coding:utf-8-*-
"""
    快速排序（Quick Sort）由图灵奖获得者Tony Hoare发明，被列为20世纪十大算法之一。冒泡排序的升级版，交换排序的一种。快速排序的时间复杂度为O(nlog(n))。

快速排序算法的核心思想：通过一趟排序将待排记录分割成独立的两部分，其中一部分记录的关键字均比另一部分记录的关键字小，然后分别对这两部分继续进行排序，以达到整个记录集合的排序目的。
快速排序的时间性能取决于递归的深度。
当pivot_key恰好处于记录关键码的中间值时，大小两区的划分比较均衡，接近一个平衡二叉树，此时的时间复杂度为O(nlog(n))。
当原记录集合是一个正序或逆序的情况下，分区的结果就是一棵斜树，其深度为n-1，每一次执行大小分区，都要使用n-i次比较，其最终时间复杂度为O(n^2)。
在一般情况下，通过数学归纳法可证明，快速排序的时间复杂度为O(nlog(n))。
但是由于关键字的比较和交换是跳跃式的，因此，快速排序是一种不稳定排序。
同时由于采用的递归技术，该算法需要一定的辅助空间，其空间复杂度为O(logn)。
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

    def quick_sort(self):
        """调用入口"""
        self.qsort(0, len(self.r) - 1)

    def qsort(self, low, high):
        """递归调用"""
        if low < high:
            pivot = self.partition(low, high)
            self.qsort(low, pivot - 1)
            self.qsort(pivot + 1, high)

    def partition(self, low, high):
        """
        快速排序的核心代码。
        其实就是将选取的pivot_key不断交换，将比它小的换到左边，将比它大的换到右边。
        它自己也在交换中不断变换自己的位置，直到完成所有的交换为止。
        但在函数调用的过程中，pivot_key的值始终不变。
        :param low:左边界下标
        :param high:右边界下标
        :return:分完左右区后pivot_key所在位置的下标
        """
        lis = self.r
        pivot_key = lis[low]
        while low < high:
            while low < high and lis[high] >= pivot_key:
                high -= 1
            self.swap(low, high)
            while low < high and lis[low] <= pivot_key:
                low += 1
            self.swap(low, high)
        return low

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

# 快速排序另外一个版本
def quick_sort(nums):
    # 封装一层的目的是方便用户调用
    def qsort(lst, begin, end):
        if begin >= end:
            return
        i = begin
        key = lst[begin]
        for j in range(begin+1, end+1):
            if lst[j] < key:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[begin], lst[i] = lst[i], lst[begin]
        qsort(lst, begin, i-1)
        qsort(lst,i+1,end)
    qsort(nums, 0, len(nums)-1)

if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.quick_sort()
    print(sqlist)
