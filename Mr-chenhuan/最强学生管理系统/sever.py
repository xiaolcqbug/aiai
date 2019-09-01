from socket import *
from sqlalchemy import Column,String,ForeignKey,create_engine,BLOB
from sqlalchemy.orm import relationship,sessionmaker,backref
from sqlalchemy.ext.declarative import declarative_base
from threading import Thread
from io import BytesIO
from os import path
import os
import pickle
import json
import re

redy = 'comeon'
add_id = 'Please add id:'
add_name = 'Please add name:'
add_age = 'Please add age:'
add_sex = 'Please add sex:'
add_address = 'Please add address:'
add_phone = 'Please add phone:'
add_clas = 'Please add clas:'
add_number = 'Please add id_number:'

base = declarative_base()

class Students(base):

    __tablename__ = '1904_python'

    s_id = Column(String(20),primary_key=True)
    s_name= Column(String(20))
    s_age= Column(String(20))
    s_sex= Column(String(3))
    s_address = Column(String(30))
    s_phone = Column(String(11))
    clas_ = Column(String(20))
    id_number = Column(String(18))
    # images = relationship('Images',cascade="delete")
    relationship('Images',cascade='all, delete-orphan', passive_deletes = True)

    # images = relationship('Images')

    def __init__(self,sid,s_name,s_age,s_sex,s_address,s_phone,clas_,id_number):
        self.s_id = sid
        self.s_name = s_name
        self.s_age = s_age
        self.s_sex = s_sex
        self.s_address = s_address
        self.s_phone = s_phone
        self.clas = clas_
        self.id_number = id_number

class Images(base):

    __tablename__ = '1904_python_images'

    image_name = Column(String(100))
    introduction_time = Column(String(50), primary_key=True)
    s_id = Column(String(100), ForeignKey('1904_python',ondelete='CASCADE'))

    # relationship('Students', backref='images')

    def __init__(self,image_name,introduction_time,s_id):
        self.image_name = image_name
        self.introduction_time = introduction_time
        self.s_id = s_id

def engine_db():
    engine = create_engine('mysql+pymysql://root:222677@localhost:3306/pythonclass')
    base.metadata.create_all(engine)
    dbsession = sessionmaker(bind = engine)
    db = dbsession()
    return db

def add(s1):
    db = engine_db()
    db.add(s1)
    db.commit()
    db.close()

def add_operation(dict1):
    sid = dict1[add_id]
    name = dict1[add_name]
    age = dict1[add_age]
    sex = dict1[add_sex]
    address = dict1[add_address]
    phone = dict1[add_phone]
    clas = dict1[add_clas]
    id_number = dict1[add_id]
    s1 = Students(sid, name, age, sex, address, phone, clas, id_number)
    add(s1)
    return 'Add_infromation --- Succeed'

def save(image_name,image_format,image_bytes,root_dir = r'D:\students_images'):
    judg = path.isdir(root_dir)
    if not judg:
        os.makedirs(root_dir)
    image_path = path.join(root_dir,image_name)      #  目录 : 根目录 \ image名称
    print(image_path)
    image_path1 = image_path+image_format   #  目录 : 根目录 \ image名称 .图片格式
    print(image_path1)
    with open(image_path1,'wb') as file:
        file.write(image_bytes)
        return image_path1

def add_images(list_images):
    print('--------')
    list_images1 = pickle.loads(list_images)
    print(list_images1)
     # 字节流  格式 时间  s_id
    bytes = list_images1[0]
    image_format = list_images1[1]
    time = list_images1[2]
    s_id = list_images1[3]
    print(s_id)
    image_path = save(s_id,image_format,bytes)
    print(image_path)
    print(s_id)
    i1 = Images(image_path,time,s_id)
    add(i1)
    return 'Add_images -- Succeed'

def delete(sid):
    print('-------')
    db = engine_db()
    db.query(Students).filter(Students.s_id == sid).delete()
    print('-------')
    db.commit()
    db.close()
    return 'Delete --- Succeed'

def update_operation(list_dict):
    global listn
    listn = []
    db = engine_db()
    print(list_dict)
    for dict1 in list_dict:
        sid = dict1['s_id']
        del dict1['s_id']
        print(dict1)
        for j in dict1:
            print('j------> ',j)
            field = dict1[j]
            print('field-----',field)
            res = db.query(Students).filter(Students.s_id == sid).one()
            print(res.s_name)
            res.s_name = field
    db.commit()
    db.close()
    return 'Update --- Succeed'

def find_all_information():
    global information_list
    global tiltle_list_information
    tiltle_list_information=[]

    db = engine_db()
    list_information = db.query(Students).all()
    for i in list_information:
        information_list = []
        information_list.append(i.s_id)
        information_list.append(i.s_name)
        information_list.append(i.s_age)
        information_list.append(i.s_sex)
        information_list.append(i.s_address)
        information_list.append(i.s_phone)
        information_list.append(i.clas_)
        information_list.append(i.id_number)
        tiltle_list_information.append(information_list)
    db.commit()
    db.close()
    print(tiltle_list_information)
    return tiltle_list_information

def find_all_images():
    global list_image_name
    list_image_name= []
    db = engine_db()
    list_images = db.query(Images).all()
    for i in list_images:
        list_image_name.append(i.image_name)
    db.commit()
    db.close()
    return list_image_name

def dispose_images():
    global listimage
    listimage = []
    list_image_name = find_all_images()
    print('list_image_name---',list_image_name)
    for i in list_image_name:
        name = path.basename(i)
        # print(name)
        # name = path.split(image_path)
        # print(name)
        with open(i,'rb') as f:
            reader = f.read()
        listimage.append(name)
        listimage.append(reader)


    return listimage

def select_find():
    pass

def four_operation(client_socket):
    list_information = find_all_information()
    list_information1 = pickle.dumps(list_information)
    client_socket.send(list_information1)

    cotinue1 = recv_information(client_socket)
    if cotinue1 == 'continue':
        listimage = dispose_images()
        listimage1 = pickle.dumps(listimage)
        client_socket.send(listimage1)

def three_operation(client_socket):
    send_information(redy,client_socket)
    list_dict = client_socket.recv(1024)
    list_dict1 = pickle.loads(list_dict)
    update_true = update_operation(list_dict1)
    send_information(update_true,client_socket)

def two_operation(client_socket):
    send_information(redy,client_socket)
    s_id = recv_information(client_socket)
    print(s_id)
    print(type(s_id))
    delete_true = delete(s_id)
    send_information(delete_true,client_socket)

def one_operation(client_socket):
    send_information(redy,client_socket)
    dict1 = recv_information(client_socket)
    one_information = json.loads(dict1)  # 字典   - -----   one_information
    succeed = add_operation(one_information)
    client_socket.send(succeed.encode('utf8'))
    byte_images = client_socket.recv(1024*1024)
    add_true = add_images(byte_images)
    send_information(add_true,client_socket)

def send_information(things,client_socket):
    things1 = things.encode('utf8')
    client_socket.send(things1)

def sever():
    ip = '127.0.0.1'
    port = 54321
    address = (ip,port)
    sever_tcp_socket = socket(AF_INET,SOCK_STREAM)
    sever_tcp_socket.bind(address)
    sever_tcp_socket.listen(30)
    return sever_tcp_socket

def recv_information(client_socket,buf_size=1024):
    masg = client_socket.recv(buf_size)
    masg = masg.decode('utf8')
    return masg

def sub_thread(client_socket):

    while True:
        code_masg = recv_information(client_socket)
        print(code_masg)
        if code_masg == '1':
            one_operation(client_socket)
        elif code_masg == '2':
            two_operation(client_socket)
        elif code_masg == '3':
            three_operation(client_socket)
        elif code_masg == '4':
            four_operation(client_socket)
        elif code_masg == '':
            break
    client_socket.close()

if __name__ == '__main__':
    sever_socket = sever()
    while 1:
        buf_size = 1024
        client_tcp_socket, client_address = sever_socket.accept()
        print('--- 来自%s的连接---'%str(client_address))
        t1 = Thread(target=sub_thread,args=(client_tcp_socket,))
        t1.start()

root_dir = r'c:\dell\vx2.png'

















