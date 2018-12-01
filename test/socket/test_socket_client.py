# -*-coding:utf-8 -*-
# File :test_socket_server.py
# Author:George
# Date : 2018/11/23
"""
    对应test_socket_server
"""
import socket
import sys

# 创建socket对象
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机
host = socket.gethostname()
# 自定义绑定端口 注意和socketServer对应
port = 9999

# 绑定 | 监听是服务器  主动连接是 客户端

def client(socket):
    # 客户端主动连接
    socket.connect((host, port))
    # 接收限定大小的数据
    msg = socket.recv(1024)
    # 关闭连接
    socket.close()

    print(msg.decode('utf-8'))


if  __name__ == "__main__":
    client(socketClient)

