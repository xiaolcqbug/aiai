from socket import *

myname = getfqdn(gethostbyname(''))
xip = gethostbyname(myname)  # 获取本地ip
cip = xip
port = 9999
address = ( cip,port)

size = 1024

tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(address)

while True:
    a = input('请输入--->:')
    tcp_client.send(a.encode('utf8'))  #发送

    res = tcp_client.recv(size) #接收
    r = res.decode('utf8')
    print('接收到来服务器的消息:',r)
    if r == 'byby':
        break
tcp_client.close()
