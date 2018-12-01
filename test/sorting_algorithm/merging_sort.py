# -*-coding:utf-8-*-
"""
    归并排序(mergin sort): 建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
"""
__author__ = 'George'
__date__ = '2018/10/20'
class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用。"""
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def merge_sort(self):
        self.msort(self.r, self.r, 0, len(self.r)-1)

    def msort(self, list_sr, list_tr, s, t):
        temp = [None for i in range(0, len(list_sr))]
        if s == t:
            list_tr[s] = list_sr[s]
        else:
            m = int((s+t)/2)
            self.msort(list_sr, temp, s,  m)
            self.msort(list_sr, temp, m+1, t)
            self.merge(temp, list_tr, s, m, t)

    def merge(self, list_sr, list_tr, i, m,  n):
        j = m+1
        k = i
        while i <= m and j <= n:
            if list_sr[i] < list_sr[j]:
                list_tr[k] = list_sr[i]
                i += 1
            else:
                list_tr[k] = list_sr[j]
                j += 1

            k += 1
        if i <= m:
            for l in range(0, m-i+1):
                list_tr[k+l] = list_sr[i+l]
        if j <= n:
            for l in range(0, n-j+1):
                list_tr[k+l] = list_sr[j+l]

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 12, 77, 34, 23])
    sqlist.merge_sort()
    print(sqlist)