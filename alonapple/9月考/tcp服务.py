
#tcp

import socket

ip = ''
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(5)
print('开始监听')
conn, addr = s.accept()
print()
data = conn.recv(1024)
print(data.decode('utf-8'))
conn.sendall(data)
conn.close()
s.close()


