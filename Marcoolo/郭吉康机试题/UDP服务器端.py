import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))

while True:

    data, addr = s.recvfrom(1024) #

    p = data.decode('utf-8').split(',')
    x = int(p[0])
    y = int(p[1])
    print(p[0], p[1])
    pos = str(x+1) + ',' + str(y+1) # 模拟服务器端下棋位置.

    s.sendto(pos.encode('utf-8'),addr)