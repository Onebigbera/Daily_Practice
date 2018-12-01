# -*-coding:utf-8 -*-
# File :test_socket.py
# Author:George
# Date : 2018/11/23
# ref_url: http://www.runoob.com/python/python-socket.html


# example
import socket  # 导入socket模块
import sys

# 创建 socket 对此昂
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本机主机名
host = socket.gethostname()
# 自定义通讯端口
port = 9999

# 绑定端口
serverSocket.bind((host, port))

# 设置最大连接数 超出后排队
serverSocket.listen(5)


def server(socket):
    # 建立起客户端连接
    clientSocket, addr = socket.accept()

    print(f'连接地址: {str(addr)}')

    msg = "welcome to socket programming"

    clientSocket.send(msg.encode('utf-8'))
    clientSocket.close()


if __name__ == "__main__":
    server(serverSocket)
