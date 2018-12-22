# -*-coding:utf-8 -*-
# File :csv_handlder_test_g.py
# Author:George
# Date : 2018/12/21
"""
    CSV文件 (Comma-Separated Value) 即为逗号分隔符模式文件，有时候也被称为字符分隔值，其文件以纯文本形式存储表格数据(数字和文本)
"""
import csv


# 读取 csv 文件内容
def read_csv_g(path):
    path = r'F:\Python_guide\Daily_Practice\test\file_operations_test_G\By_txt.csv'
    # 打开文件
    csvFile = open(path, newline='', encoding='utf-8')
    # 读取打开的 csv 文件流 获取文件内容
    csvReader = csv.reader(csvFile)
    # 打印文件内容 查看其中每一项的字符类型和按照索引取值
    [print(row,type(row),row[1]) for row in csvReader]
    # 关闭文件
    csvFile.close()


def read_csv_V(path):
    # 使用 with open() 格式 操作文件同样可行 而且末尾不需要手动关闭文件
    path = r'F:\Python_guide\Daily_Practice\test\file_operations_test_G\By_txt.csv'
    with open(path, newline='', encoding='utf-8') as f:
        csvReader = csv.reader(f)
        [print(row) for row in csvReader]


# 将特定内容写入到生成 csv 文件  当 csv 文件不存在时 就会常见csv文件
def write_csv_G(path):
    path = r'F:\Python_guide\Daily_Practice\test\file_operations_test_G\test_txt.csv'
    # 打开文件 不存在文件则会创建
    csvFile = open(path, 'w', newline='')
    # 利用 csv 模块自带的 write 函数
    """
        dialect : 方言，同源语， 表示按照何种文件方式操作  选取 excel
    """
    writer = csv.writer(csvFile, dialect='excel')
    # 写入一行数据  其每一行都是以元祖格式为单位
    writer.writerow(('名称', '网址'))
    # row 中每个元素为元祖
    rows = [
        ('baidu', 'https://www.baidu.com/'),
        ('Bing', 'https://cn.bing.com/?mkt=zh-CN')
    ]
    # 写入多行
    writer.writerows(rows)
    csvFile.close()


# 在末尾追加
def append_csv_G(path):
    path = r'F:\Python_guide\Daily_Practice\test\file_operations_test_G\test_txt.csv'
    with open(path, 'a', newline='') as f:
        writer = csv.writer(f)
        # 外部的数据格式也可以是列表 只需要是可迭代对象 就可以
        rows = (
            ('Google', 'http://www.google.com/'),
            ('Amazon', 'http://www.amazon.com/'),
        )
        writer.writerows(rows)


if __name__ == "__main__":
    path_read = r'F:\Python_guide\Daily_Practice\test\file_operations_test_G\By_txt.csv'
    read_csv_g(path_read)

    # path_write = r'F:\Python_guide\Daily_Practice\test\file_operations_test_G\test_txt.csv'
    # write_csv_G(path_write)

    # append_path = r'F:\Python_guide\Daily_Practice\test\file_operations_test_G\test_txt.csv'
    # append_csv_G(append_path)
