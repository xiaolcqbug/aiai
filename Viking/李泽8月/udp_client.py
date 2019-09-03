import socket

ip = '192.168.1.13'
port = 8080
adder = ('192.168.1.13', 8080)

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
text = input('输入:')
udp_socket.sendto(text.encode('utf8'), adder)
mess, recv_adder = udp_socket.recvfrom(1024)
print(mess.decode('utf8'))
udp_socket.close()
