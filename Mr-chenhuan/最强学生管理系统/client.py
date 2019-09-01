from datetime import datetime
import image_show
from socket import *
import pickle
from os import path
import json
import re
import os


add_str = 'Please add '
redy = 'comeon'
continue1 = 'continue'

def add_label():
    global list_clomn
    list_clomn = ['id:','name:','age:','sex:','address:','phone:','clas:','id_number:']
    for i in range(len(list_clomn)):
        list_clomn[i] = add_str + list_clomn[i]
    return list_clomn

def bytes_images(path_str):
    with open(path_str,'rb') as f:
        pattern = '[.][a-zA-Z]+'
        res = re.search(pattern, path_str)
        image_format = res.group()
        reader = f.read()
        return reader,image_format

def send_dict1(list1_label,client_socket):
    for i in list1_label:
        information = input(i)
        dict1[i] = information
    dict2 = json.dumps(dict1)
    dict3 = dict2.encode('utf8')
    client_socket.send(dict3)
    return dict1

def image_path():
    image_path = 'image_path:'
    image_question = add_str+image_path
    path_image = input(image_question)
    return path_image

def sendimage_time():
    now = datetime.now()
    msg = "%d年-%d月-%d日-%d时-%d秒-%d分-%d毫秒" \
          % (now.year, now.month, now.day,
             now.hour, now.minute, now.second,
             now.microsecond)
    return msg

def send_image(dict1):
    global list_image
    list_image = []
    image_path1 = image_path()                          # 输入的图片路径
    bytes1,image_format = bytes_images(image_path1)     # 将路径中的图片读出返回 字节流及 图片格式
    send_time = sendimage_time()
    list_image.append(bytes1)
    list_image.append(image_format)
    list_image.append(send_time)
    list_image.append(dict1['Please add id:'])
    print(list_image)
    return list_image

def init():
    ip = '127.0.0.1'
    port = 54321
    address = (ip, port)
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(address)
    return client_socket

def send_information(things,client_socket):
    things1 = things.encode('utf8')
    client_socket.send(things1)

def recv_information(client_socket,buf_size=1024):
    masg1 = client_socket.recv(buf_size)
    masg = masg1.decode('utf8')
    return masg

def delete_question():
    delete_sid = input('Delete s_id:')
    return delete_sid

def update_question():
    global change_dict
    list_dict = []
    change_number = input('How many student information should I change?:')
    change_number1 = int(change_number)
    while change_number1 > 0:
        sid = input('To change the student sid:')                           # 1
        fields_number = input('How many field should I change?:')           # 2
        fields_number1 = int(fields_number)
        change_dict = {}
        while fields_number1 > 0:

            before_fields = input('The field to be modified:')              # name   , age
            after_fields = input('The changed information:')               # 张    , 18
            change_dict['s_id'] = sid                                     # {'sid':1,'name':张,'age':18}
            change_dict[before_fields] = after_fields
            fields_number1 -= 1
        list_dict.append(change_dict)
        change_number1 -= 1
    return list_dict

def dispose_findall_images(listimages,save_dir=os.getcwd()):
    global listimages_path
    listimages_path = []
    long_listimages = len(listimages)
    i = 0
    while  i < long_listimages:
        image_name = listimages[i]
        image_path = path.join(save_dir, image_name)  # 目录 : 根目录 \ image名称
        i += 1
        with open(image_path,'wb') as file:
            file.write(listimages[i])
            listimages_path.append(image_path)
        i +=1
    # print(listimages_path)
    return listimages_path


def dispose_find_all(listimages,list_information):
    listimages_path = dispose_findall_images(listimages)
    title_students_information = dict(zip(listimages_path,list_information))
    return title_students_information

def show_allinformation(title_students_information):
    for i in title_students_information:
        print(title_students_information[i])

def four_operation(client_socket):
    list_information = client_socket.recv(1024)
    list_information1 = pickle.loads(list_information)
    send_information(continue1,client_socket)
    listimages = client_socket.recv(1024*1024)
    listimages1 = pickle.loads(listimages)
    title_students_information = dispose_find_all(listimages1,list_information1)
    # show_allinformation(title_students_information)
    image_show.show(title_students_information)
def three_operation(client_socket):
    masg = recv_information(client_socket)
    if masg == redy:
        list_dict = update_question()
        list_dict1 = pickle.dumps(list_dict)
        client_socket.send(list_dict1)
        update_true = recv_information(client_socket)
        print(update_true)

def two_operation(client_socket):
    masg = recv_information(client_socket)
    delete_sid = delete_question()
    if masg == redy:
        send_information(delete_sid,client_socket)
        delete_true = recv_information(client_socket)
        print(delete_true)

def one_operation(client_socket):
    masg = recv_information(client_socket)
    list_label = add_label()
    if masg == redy:
        dict1 = send_dict1(list_label, client_socket)
        add_true = recv_information(client_socket)
        print(add_true)
        print('Then--image')
        list_image = send_image(dict1)
        print(list_image)
        list_image1 = pickle.dumps(list_image)
        print(list_image1)
        client_socket.send(list_image1)
        add_true2 = recv_information(client_socket)
        print(add_true2)

def send(client_socket):
    global dict1
    global list1
    dict1 = {}
    while 1:
        code = input('输入指令:')
        if code == '1':
            send_information(code,client_socket)
            one_operation(client_socket)
        elif code == '2':
            send_information(code, client_socket)
            two_operation(client_socket)
        elif code == '3':
            send_information(code, client_socket)
            three_operation(client_socket)
        elif code == '4':
            send_information(code, client_socket)
            four_operation(client_socket)
        elif code =='over':
            break

while 1:
    buf_size = 1024
    client_socket = init()
    send(client_socket)
client_socket.close()





















