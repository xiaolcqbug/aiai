#�ļ����նˣ�����ˣ�file_receive.py��

import socket

#ʵ����
sk = socket.socket()
#�������ӵ�ip��port
ip_port = ('127.0.0.1',9999)
#�󶨶˿�
sk.bind(ip_port)
#���������
sk.listen(5)
#����ѭ����������
conn, address = sk.accept()
print("�ļ����տ�ʼ")
while True:
    with open('file','ab') as f:
        #��������
        data = conn.recv(1024)
        if data == b'quit':
            break
        #д���ļ�
        f.write(data)
        #������ɱ�־
        conn.send('success'.encode())
print("�ļ��������")
#�ر�����
sk.close()

#�ļ����Ͷˣ��ͻ��ˣ�file_send.py��

import socket

#ʵ����
sk = socket.socket()
#�������ӵ�ip��port
ip_port = ('127.0.0.1',9999)
#����������
sk.connect(ip_port)
#�ļ��ϴ�
#���ļ�
with open('D:\pythonwork\socket\socket_server_tcp2.py','rb') as f:
    #��ÿһ�ηָ��ļ��ϴ�
    for i in f:
        sk.send(i)
        #�ȴ�������ɱ�־
        data=sk.recv(1024)
        #�ж��Ƿ������������
        if data != b'success':
            break
#������˷��ͽ����ź�
sk.send('quit'.encode())
