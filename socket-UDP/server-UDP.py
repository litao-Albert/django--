#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/20 12:01
# software:PyCharm Community Edition
import socket

# 1、创建套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 2、绑定端口
sock.bind(('127.0.0.1',15801))

date,addrs = sock.recvfrom(521)
# 发送数据，到指定得地址
sock.send("server".encode(),('127.0.0.1',8002))
# 打印信息和地址
print(date.decode(),addrs)
sock.close()
