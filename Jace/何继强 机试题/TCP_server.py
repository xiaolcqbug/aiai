from socket import *


myname = getfqdn(gethostbyname(''))
xip = gethostbyname(myname)  # 获取本地ip
cip = xip
port = 9999
address = ( cip,port)
size = 1024

socket_TCP = socket(AF_INET,SOCK_STREAM)
socket_TCP.bind(address)  #绑定
socket_TCP.listen(5) #监听
rip,con = socket_TCP.accept()
while True:
    message = rip.recv(size)
    res = message.decode('utf8')
    print('接收到来自地址{}消息{}'.format(con,res))
    if res == 'over':
        break
    message2 = input('请输入:')
    rip.send(message2.encode('utf8'))
socket_TCP.close()

