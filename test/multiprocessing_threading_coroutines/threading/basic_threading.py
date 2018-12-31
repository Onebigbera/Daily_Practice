# -*-coding:utf-8 -*-
# File :basic_threading.py
# Author:George
# Date : 2018/12/22
"""
    多线程并行执行任务
"""
import threading
from time import ctime, sleep


# 定义的学习的方法
def read_g(book, loop):
    for i in range(loop):
        print("Start reading %s %s" % (book, ctime()))
        sleep(2)


# 定义写的方法
def write_g(book, loop):
    for i in range(loop):
        #  .format() 格式符使用
        print("Starting writing {} {} %s" .format (book, ctime()))
        sleep(2)


def main():
    # 定义一个存放线程对象的列表
    thread = []
    # 实例化线程对象
    read_thread = threading.Thread(target=read_g, args=('python', 20))
    # 将线程对象放到容器中
    thread.append(read_thread)

    write_thread = threading.Thread(target=write_g, args=('java', 30))
    thread.append(write_thread)
    # 让容器中线程开始执行
    [thread_item.start() for thread_item in thread]

    # 主线程等待线程执行结束 释放资源  这一步必须 防止内存泄露
    [thread_item.join() for thread_item in thread]


if __name__ == "__main__":
    # 可以看出来 其为一起执行
    main()
