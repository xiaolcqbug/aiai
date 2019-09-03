import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

x = input('请输入x坐标:')
y = input('请输入y坐标:')
data = str(x) + ',' + str(y)

s.sendto(data.encode('utf-8'), ('127.0.0.1', 8888))

data2, addr = s.recvfrom(1024)

s.close()
