from socket import *

ip = 'localhost'
port = 46283
add = (ip, port)
buf_size = 1024

sock1 = socket(AF_INET, SOCK_STREAM)
sock1.bind(add)
sock1.listen(5)

print('等待客户端连接中......')
c_sock, c_add = sock1.accept()

while 1:
    data = c_sock.recv(buf_size)
    data = data.decode("utf8")
    print('来自客户端的消息：{}'.format(data))
    print('来自%s的连接' % str(c_add))

    msg_sever = input('请服务端输入---->')
    c_sock.send(msg_sever.encode('utf8'))
