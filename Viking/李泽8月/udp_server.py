import socket

ip = '192.168.1.13'
port = 8080
adder = (ip, port)


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(adder)
mess, recv_adder = udp_socket.recvfrom(1024)
print(mess.decode('utf8'))
udp_socket.sendto(mess, recv_adder)
udp_socket.close()
