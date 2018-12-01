# -*-coding: utf-8 --
"""
    归并排序的另外一个版本
    归并排序对原始序列元素分布情况不敏感，其时间复杂度为O(nlogn)。
归并排序在计算过程中需要使用一定的辅助空间，用于递归和存放结果，因此其空间复杂度为O(n+logn)。

归并排序中不存在跳跃，只有两两比较，因此是一种稳定排序。

总之，归并排序是一种比较占用内存，但效率高，并且稳定的算法。
"""
def merge(lfrom, lto, low, mid, high):
    """
    两段需要归并的序列从左往右遍历，逐一比较，小的就放到
    lto里去，lfrom下标+1，lto下标+1，然后再取，再比，再放，
    最后lfrom里的两段比完了，lto里留下的就是从小到大排好的一段。
    :param lfrom: 原来的列表
    :param lto: 缓存的列表
    :param low: 左边一段的开头下标
    :param mid: 左右两段的中间相隔的下标
    :param high: 右边一段的最右下标
    :return:
    """
    i, j, k = low, mid, low
    while i < mid and j < high:
        if lfrom[i] <= lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:
        lto[k] = lfrom[j]
        j += 1
        k += 1


def merge_pass(lfrom, lto, llen, slen):
    """
    用来处理所有需要合并的段，这需要每段的长度，以及列表的总长。
    最后的if语句处理表最后部分不规则的情况。
    :param lfrom: 原来的列表
    :param lto: 缓存的列表
    :param llen: 列表总长
    :param slen: 每段的长度
    :return:
    """
    i = 0
    while i+2*slen < llen:
        merge(lfrom, lto, i, i+slen, i+2*slen)
        i += 2*slen
    if i+slen < llen:
        merge(lfrom, lto, i, i+slen, llen)
    else:
        for j in range(i, llen):
            lto[j] = lfrom[j]


def merge_sort(lst):
    """
    主函数。
    先安排一个同样大小的列表，作为辅助空间。
    然后在两个列表直接做往复的归并，每归并一次slen的长度增加一倍，
    逐渐向llen靠拢，当slen==llen时说明归并结束了。
    归并完成后最终结果可能恰好保存在templist里，因此代码里做两次归并，
    保证最后的结果体现在原始的lst列表里。
    :param lst: 要排序的原始列表
    :return:
    """
    slen, llen = 1, len(lst)
    templist = [None]*llen
    while slen < llen:
        merge_pass(lst, templist, llen, slen)
        slen *= 2
        merge_pass(templist, lst, llen, slen)
        slen *= 2