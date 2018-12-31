# -*-coding:utf-8 -*-
# File :logDemo.py
# Author:George
# Date : 2018/12/29
"""
    测试使用 python 中的logging模块 简单地生成log日志

"""
import logging
import os
import time


def test_log():
    # 第一步：创建一个logger对象
    logger = logging.getLogger()
    # 设置自定义的logger对象的等级
    logger.setLevel(logging.INFO)

    # 第二步：创建一个handler，用于写入日志文件
    createTime = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    # 定义存在日志的文件夹
    log_path = os.path.dirname(os.getcwd()) + '/logG/logfile/'
    print(os.getcwd())
    print(os.path.dirname(os.getcwd()))
    print(os.path.dirname(os.getcwd()) + '/log/')
    # 拼接出log文件的路径
    log_name = log_path + createTime + '.log'
    log_file = log_name  # 程序中都是用路径来标识文件的
    # 产生一个 file_handler?
    fh = logging.FileHandler(log_file, mode='w')
    fh.setLevel(logging.DEBUG)

    # 第三步：定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)

    # 第四步：将logger添加到handler里面
    logger.addHandler(fh)

    # 日志内容
    logger.debug('this is a logger debug message')
    logger.info('this is a logger info message')
    logger.warning('this is a logger warning message')
    logger.error('this is a logger error message')
    logger.critical('this is a logger critical message')


if __name__ == "__main__":
    test_log()
