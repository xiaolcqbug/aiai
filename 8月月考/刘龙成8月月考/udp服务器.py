from socket import *

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(('localhost', 9999))
data, con_client = udp_server.recvfrom(1024)
print('from:', con_client, ':', data)
