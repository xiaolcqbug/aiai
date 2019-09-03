from socket import *

tcp_client = socket()
tcp_client.connect(('localhost',8888))
tcp_client.send(b'123')
data = tcp_client.recv(1024)
print(data)
tcp_client.close()