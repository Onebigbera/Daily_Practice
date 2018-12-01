
#coding:utf-8

import socket
"""
#创建socket对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP地址
sock.bind(("",8001))
#设置最大监听数量
sock.listen(3)
print("服务器已经启动.....")
#接收信息
con,add = sock.accept()
print(con,add)
print("%s已经链接上...."%add[0]) #con表示sock对象接收的信息，add表示SOCK对象接收的IP地址

#打印接收过来的信息
recvs = con.recv(512) #括号中的数字表示其每次接受的数字上限
print(recvs.decode("utf-8")) #需要解码后打印
#发送信息给客户端
data = input("请输入要发送的信息:")
con.send(data.encode("utf-8")) #转码后发送

sock.close()
"""

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(("",8001))
# sock.listen(5)
# print("服务器已经启动....")
# a = 0
# while a == 0:
#     con,add = sock.accept()
#     while True:
#         recvs = con.recv(512) #每次接受的字节上限为512
#         print(recvs.decode("utf-8"))
#         if recvs.decode("utf-8") == "break":
#             break
#         sends = input("请输入要发送的信息:")
#         con.send(sends.encode("utf-8")) #进行编码后进行发送
#         if sends == "break":
#             a = 1 # 县赋值，再退出
#             break
#
# sock.close()

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn',80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')
# buffer = []
# while True:
# 	d = s.recv(1024)
# 	if d:
# 		buffer.append(d)
# 	else:
# 		break
# data = b''.join(buffer)
# s.close()
#
# header,html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# with open('sina.html','wb') as f:
# 	f.write(html)

#创建socket对象
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定IP地址和端口号
sock.bind(("",8003))

while True:
    #接收发送过来的信息和IP地址还有端口号
    con,add = sock.recvfrom(512)
    print("%s is connected!"%(add[0]))
    print(con.decode("utf-8"))
    # print(add)
    #输入要发送的信息
    sends = input("请输入要发送的信息:")
    #注意  发送的信息要进行编码
    sock.sendto(sends.encode("utf-8"),("127.0.0.1",8002)) #sendto 函数中有一个参数为（对应的ip地址，端口号）
    if sends == "break":
        break
sock.close()

