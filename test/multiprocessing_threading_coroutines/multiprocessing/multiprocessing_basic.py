# -*-coding:utf-8 -*-
# File :multiprocessing_basic.py
# Author:George
# Date : 2018/12/22
"""
    程序在数据集上的一次运行就是进程，计算机就是基于进程/线程模型构建的。
"""

import multiprocessing
from time import sleep,ctime

# 定义生产的方法
def product_g(product, loop):
    for i in range(loop):
        print("I have created great {} at {}".format(product, ctime()))
        sleep(1)


# 定义消费的方法
def consumer_g(product, loop):
    for i in range(loop):
        print("I have consumed {} at {}".format(product, ctime()))
        sleep(1)

def main():
    # 定义存放进程对象的容器
    process_list = []
    # 实例化进程对象
    product_process = multiprocessing.Process(target=product_g, args=('tools', 6))
    process_list.append(product_process)

    consume_process = multiprocessing.Process(target=consumer_g, args = ('tools', 6))
    process_list.append(consume_process)

    # 运行
    [process.start() for process in process_list]
    # 主进程等待子进程结束 避免孤儿进程
    [process.join() for process in process_list]

if __name__ == "__main__":
    main()