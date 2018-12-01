# -*-coding:utf-8 -*-
# File :os_test_g.py
# Author:George
# Date : 2018/11/24

"""
    os模块有三种 posix(适用于unix操作系统) nt(win) mac()
    os对进程和进程运行环境进行管理, os模块还可以处理大部分文件系统操作:
    删除、重命名文件,遍历目录树，以及管理文件访问权限
    os 和 sys 区别:
    OS负责程序与操作系统的交互
    os.path是一个模块，提供一些方法函数
    SYS 负责程序与python解释器的交互
    sys.path 常用的环境变量 PATH


"""
#
import os

# 显示正在使用的平台 windows用nt表示   Unix和Linux用posix
import time

print(os.name)

# 获取当前进程的工作目录 当前python脚本工作的目录路径
# print(os.getcwd())

# 更改当前工作路径
# os.chdir(path='xxx')

# 获取指定目录下的所有文件和目录名的一个列表
# print(os.listdir('/.'))

# 返回上级目录
# os.chdir('..')
print(os.getcwd())

# walk() 函数返回三个返回值 这个函数会返回三个值
print(os.walk('./'))


# 创建并打开一个('w+b')一个新的临时文件
# os.tmpfile()

# makedirs(可以建递归的目录)
# os.chdir('F:/Python_guide/Daily_Practice/test/sys_module')
# print(os.getcwd())
# os.makedirs('./test_os')

# mkdir 创建目录 只能建一层
# os.mkdir('./test_mkdir')

# removedirs 删除指定目录，如果目录为空就删除
# os.removedirs('./test_os')

# rmdir 只能删除单级目录为空的文件夹
# os.rmdir('./test_mkdir')

# listdir 列出指定文件夹下所有的文件夹和问价包括隐藏文件 以列表方式返回
# print(os.listdir('F:/Python_guide/Daily_Practice/test'))

# remove 删除指定的文件
# os.remove('F:/Python_guide/Daily_Practice/test/sys_module/test_how.py')

# rename 修改文件夹名字或者文件名称
# os.rename('test_name.py', 'test_name_new.py')

# stat 统计文件的具体信息
# print(os.getcwd())
# print(os.stat('F:/Python_guide/Daily_Practice/test/sys_module'))

# sep输出当前操作系统的路径分隔符
# print(os.sep)

# linesep 输出当前操作系统的行终止符 win是\r\n linux是\n
# print(os.linesep)

# system运行shell命令 直接显示结果
# os.system('notepad')

# os.path.split 把路径分为两个部分 1个是目录路径 1个是文件名
# print(os.path.split(r'F:/Python_guide/Daily_Practice/test/sys_module/test_sys.py'))

# os.path.dirname拿split分隔的第一个元素 os.path.basename 拿 split分隔的第二个元素

# print(os.path.split(r'F:\Python_guide\Daily_Practice\test\sys_module/test_sys.py'))
# print(os.path.dirname(r'F:\Python_guide\Daily_Practice\test\sys_module/test_sys.py'))
# print(os.path.basename(r'F:\Python_guide\Daily_Practice\test\sys_module/test_sys.py'))

# os.path.exists 判断路径是否存在
# 路径指向目录
# print(os.path.exists(r'F:\Python_guide\Daily_Practice\test\sys_module'))
# 路径指向一个py文件
# print(os.path.exists(r'F:\Python_guide\Daily_Practice\test\sys_module\test_sys.py'))

# os.apth.isabs 如果是绝对路径就返回True 否则返回False
# print(os.path.isabs('F:\Python_guide\Daily_Practice\test\sys_module'))

# os.path.isfile 判断一个文件是否存在 存在返回True 否则为False
# print(os.path.isfile(r'F:\Python_guide\Daily_Practice\test\sys_module'))
# print(os.path.isfile(r'F:\Python_guide\Daily_Practice\test\sys_module\os_test_g.py'))

# os.path.isdir() 判断目录是否存在 存在为True 否则为False
# print(os.path.isdir('F:\Python_guide\Daily_Practice\test\sys_module'))

# os.path.join() 路径拼接 (重要常用)
# print(os.path.join(r'F:\Python_guide\Daily_Practice', 'test\sys_module'))

# os.path.getmtime() 返回path的文件或者路径的最后修改时间 结果是时间戳 得到时间戳时间后 再转化为字符串时间 modify 修改
# print(os.path.getmtime('os_test_g.py'))

# 输出文件|目录的创建时间
# print(os.path.getctime('os_test_g.py'))

# 将最后修改文件的时间以固定格式化时间显示   2018-11-24 18:27:56
# print(time.strftime('%Y-%m-%d %X', time.localtime(os.path.getmtime('os_test_g.py'))))
