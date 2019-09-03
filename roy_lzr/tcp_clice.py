from socket import *
ip='127.0.0.1'
port=8090
address=(ip,port)
buf_size=1024

sockets=socket(AF_INET,SOCK_STREAM)
sockets.connect(address)

while True:
    msg=input('>>>')
    sockets.send(msg.encode('utf8'))
    if msg=='break':
        break
    add=sockets.recv(buf_size)
    print('服务端说:',add.decode('utf8'))
sockets.close()
