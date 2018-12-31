#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/20 10:57
# software:PyCharm Community Edition
import socket
print("正在连接中..........")
def server_TCP(sock,addrs):
    # 接收客户端发来得信息,并发送数据
    print('Accept new connection from %s:%s'%addr)
    sock.send(b'hello,I am server!')
    info = sock.recv(1024).decode()
    while info != 'exit':
        # print("客户端："+info)
        #向客户端发送数据
        send_mes = input(">>>>>:")
        sock.send(send_mes.encode())
        if send_mes == 'exit':
            break
        # 接收信息
        info = sock.recv(1024).decode()
        sock.close()
if __name__ == "__main__":
    # 1、创建套接字socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2、绑定套接字，参数为双元组，如果为空不写代表本地所有得IP
    s.bind(('127.0.0.1',9010))
    # 3、监听，最大断开为5
    s.listen(5)
    sock,addr = s.accept()
    server_TCP(sock,addr)

