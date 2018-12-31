# -*-coding:utf-8 -*-
# File :exceptTrace.py
# Author:George
# Date : 2018/12/31
"""
    利用logging模块记录捕捉到的异常
"""
import os
import time
import logging


def exceptTraceG():
    # 创建一个 logger 对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建一个 handler，用于写入日志文件
    create_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd()) + '/logG/logfile/'
    log_name = log_path + create_time + '.log'
    fh = logging.FileHandler(log_name, mode='a')
    fh.setLevel(logging.DEBUG)

    # 定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # 设置使用 logger.XX 来记录错误，这里的"error"可以根据所需要的级别修改
    try:
        with open("/path/to/does/not/exit", 'rb') as fr:
            file = fr.read()
    except BaseException as e:
        logger.error("Failed to open file", exc_info=True)


if __name__ == "__main__":
    exceptTraceG()
