import socket
# 1、创建一共套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2、套接字连接
sock.connect(('127.0.0.1',9005))   #  里面是一个元组
# 3、接收和发送信息
info = ''
while info!='exit':
    message = input(">>>>>>")
    sock.send(message.encode())
    if message == 'exit':
        break
    #  接收服务器发来的消息
    info = sock.recv(1024).decode()
    print('服务器：'+info)
    # 关闭套接字
    sock.close()