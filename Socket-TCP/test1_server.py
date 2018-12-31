import  socket

print("正在连接..............")
def Test_server(con,addr):
    # 接客户端发来的信息
    info = con.recv(1024).decode()
    while info !='exit':
        # print('客户端:'+info)
        # 向客户端发送数据
        mesg = input('>>>>>>>>>:')
        con.send(mesg.encode())
        if mesg == 'exit':
            break
        #接收客户端发来的消息
        info = con.recv(1024).decode()
        print('客户端:'+info)
        con.close()
if __name__ == '__main__':
    # 1.创建套接字
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定IP
    sock.bind(('127.0.0.1',9005))
    # 3.监听
    sock.listen(5)
    # 4.接收
    con,addr = sock.accept()
    #  调用函数把参数传递过去
    Test_server(con,addr)
