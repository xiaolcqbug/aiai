from socket import *

tcp_server = socket()
tcp_server.bind(('localhost',8888))
tcp_server.listen(5)
con_client,cip = tcp_server.accept()
print(cip)
data = con_client.recv(1024)
print(data)
con_client.send(b'123456')
con_client.close()