# -*-coding:utf-8 -*-
# File :logRolll_overdueDelete.py
# Author:George
# Date : 2018/12/31
"""
    日志就像是系统运行的轨迹手册，通过日志我们可以分析系统运行情况作出诊断，但是过多的大量日志势必会占用系统存储资源，因此我们需要设置过期删除
    ref: https://www.cnblogs.com/CJOKER/p/8295272.html
"""
import logging
import time
import re
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler


def backrollG():
    # 定义日志打印格式
    log_fmt = '%(asctime)s\tFile \"%(filename)s",line %(lineno)s\t%(levelname)s:%(message)s'
    formatter = logging.Formatter(log_fmt)

    # 创建 TimeRotatingFileHandler对象
    log_file_handler = TimedRotatingFileHandler(filename='ds_update', when="D", interval=2, backupCount=2)

    # 设置 handler
    log_file_handler.suffix = "%Y-%m-%d_%H_%M.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-d{2}_d{2}_d{2}.log$")

    # handler 中设置 formatter
    log_file_handler.setFormatter(formatter)
    # 设置logger等级
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()
    # 使用log_file_handler处理 log | 向log中添加handler
    log.addHandler(log_file_handler)

    # 测试循环打印日志
    log_content = "test log"
    count = 0
    while count < 30:
        log.error(log_content)
        time.sleep(5)
        count = count + 1
    log.removeHandler(log_file_handler)


if __name__ == "__main__":
    backrollG()
