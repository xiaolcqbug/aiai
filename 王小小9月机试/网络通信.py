#文件接收端（服务端）file_receive.py：

import socket

#实例化
sk = socket.socket()
#定义连接的ip和port
ip_port = ('127.0.0.1',9999)
#绑定端口
sk.bind(ip_port)
#最大连接数
sk.listen(5)
#进入循环接收数据
conn, address = sk.accept()
print("文件接收开始")
while True:
    with open('file','ab') as f:
        #接收数据
        data = conn.recv(1024)
        if data == b'quit':
            break
        #写入文件
        f.write(data)
        #接受完成标志
        conn.send('success'.encode())
print("文件接收完成")
#关闭连接
sk.close()

#文件发送端（客户端）file_send.py：

import socket

#实例化
sk = socket.socket()
#定义连接的ip和port
ip_port = ('127.0.0.1',9999)
#服务器连接
sk.connect(ip_port)
#文件上传
#打开文件
with open('D:\pythonwork\socket\socket_server_tcp2.py','rb') as f:
    #按每一段分割文件上传
    for i in f:
        sk.send(i)
        #等待接收完成标志
        data=sk.recv(1024)
        #判断是否真正接收完成
        if data != b'success':
            break
#给服务端发送结束信号
sk.send('quit'.encode())
