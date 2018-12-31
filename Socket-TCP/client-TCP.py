#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/20 10:49
# software:PyCharm Community Edition
import socket
# # 1、创建一个套接字 并以tcp连接
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 2、绑定套接字，参数为双元组，如果写空代表本地所有得IP
# sock.connect(('127.0.0.1',9001))
# # 3、接收服务端发来得数据
# print(sock.recv(521).decode())
# # 3、发送数据
# sock.send('Hi'.encode())
# # 5、关闭套接字
# sock.close()

#创建一个套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#套接字连接
sock.connect(('127.0.0.1',9010))
print('已经建立连接')
info= ''
while info != 'exit':
    send_mes = input('>>>>')
    sock.send(send_mes.encode())
    if send_mes == 'exit':
        break
    # 得到服务器输入得信息
    info = sock.recv(1024).decode()
    print('服务器：'+ info)
    sock.close()
