#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/20 12:10
# software:PyCharm Community Edition
import socket

#创建套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定端口
sock.bind(('127.0.0.1',8002))
# 发送信息到指定得地址
date,addr = sock.recvfrom(521)
sock.send('client'.encode(),('127.0.0.1',15801))
print(date.decode(),addr)
sock.close()