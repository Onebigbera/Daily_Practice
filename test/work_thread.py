# _*_ coding:utf-8 _*_
"""
 Thread: 线程
 进程：
    程序运行的基本单元，最小单位。

 线程：

 协程：


"""

# 进程示范
from multiprocessing import Process
import time
import random


def talk(name):
    print('%s is talking' % name)
    time.sleep(random.randint(1, 3))
    print('%s has finished his talk ' % name)


if __name__ == "__main__":
    # 实例化进程实例
    p1 = Process(target=talk, args=('Alex',))
    p2 = Process(target=talk, args=('Tom',))
    p3 = Process(target=talk, args=('Mike',))
    p4 = Process(target=talk, args=('Rich',))

    p_list = [p1, p2, p3, p4]
    for p in p_list:
        p.start()

    for p in p_list:
        p.join()

"""
    演示一个对比加锁和不加锁对线程影响的案例
"""
import threading
import time

# 实例化锁对象
lock = threading.Lock()
num = []


# 加了进程锁的函数
def test1(n):
    # 让锁生效
    lock.acquire()
    # 向列表中添加
    num.append(n)
    print(num)
    # 开锁 锁释放
    lock.release()


# 不加进程锁的函数
def test(n):
    num.append(n)
    print(num)


def main():
    for i in range(10):
        # 执行不加锁的程序
        # th = threading.Thread(target=test, args=(i,))
        # 执行加了锁的程序
        th = threading.Thread(target=test1, args=(i,))
        th.start()


if __name__ == '__main__':
    main()
