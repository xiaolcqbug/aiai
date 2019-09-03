from socket import *
ip='127.0.0.1'
port=8090
address=(ip,port)
buf_size=1024

sockets=socket(AF_INET,SOCK_STREAM)
sockets.bind(address)
sockets.listen(5)
sock_ip,cust_link=sockets.accept()

while True:
    rres = sock_ip.recv(buf_size).decode('utf8')
    print('客户端说:',rres)
    if  rres=='break':
        break
    res = input('>>>')
    sock_ip.send(res.encode('utf8'))

sock_ip.close()
sockets.close()
