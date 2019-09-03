import tkinter
from tkinter import *
from PIL import Image,ImageTk


#  Image.size	图像高度与宽度，单位是像素（px）,返回值是二元元组（tuple）
#  Image.thumbnail(size)	创建图像的缩略图，size是缩略图尺寸的二元元组
#  Image.resize(size)	按size大小调整图像，生成副本
#  Image.rotate(angle)	按angle角度旋转图像，生成副本
#  Image.split() 根据GRB图像的每个颜色通道，返回图像副本

def Action(win):
    font_show = ('楷体', 20)
    label_show = tkinter.Label(win, text='Display all 学生信息!', font=font_show)
    label_show.place(x=200,y = 30)

def base_information(win,font_code,list_information):
    global base_list
    y1 = 120
    base_list = ['s_id:','s_name:','s_age:','s_sex:','s_address:','s_phone:','clas:','id_number:']
    for i in range(4):
        label_code = tkinter.Label(win,text=base_list[i],font=font_code)
        label_code.place(x=400,y=y1)
        label_code = tkinter.Label(win, text=list_information[i], font=font_code)
        label_code.place(x=500, y=y1)
        y1+=60

def input1(win,font_code,list_information):
    label_code = tkinter.Label(win, text=list_information[4], font=font_code)
    label_code.place(x=260, y=380)
    label_code = tkinter.Label(win, text=list_information[5], font=font_code)
    label_code.place(x=540, y=380)
    label_code = tkinter.Label(win, text=list_information[6], font=font_code)
    label_code.place(x=220, y=460)
    label_code = tkinter.Label(win, text=list_information[7], font=font_code)
    label_code.place(x=600, y=460)

def extend_information(win,font_code,list_information):
    x1 = 150
    y1 = 380
    for i in range(4,6):
        label_code = tkinter.Label(win,text=base_list[i],font=font_code)
        label_code.place(x=x1,y=y1)
        x1 += 300
    x1 = 150
    y1 += 80
    for i in range(6,8):
        label_code = tkinter.Label(win,text=base_list[i],font=font_code)
        label_code.place(x=x1,y=y1)
        x1 += 350
    input1(win,font_code,list_information)

def show_all(win,font_code,list_information):
    base_information(win, font_code, list_information)
    extend_information(win, font_code, list_information)


def button_all(win,font_code,list_information,return_button_state,next_button_state):
    def show_all1():
        show_all(win, font_code, list_information)
    print(return_button_state)
    print(next_button_state)
    button1 = tkinter.Button(win,text='next', font=('楷体', 15), state=next_button_state,width=10,command=show_all1)
    button1.place(x=440, y=540)

    button2 = tkinter.Button(win,text='<----', font=('楷体', 15),state=return_button_state, width=5,command = show_all1)
    button2.place(x=5, y=5)

def first_button_state():
        return_button_state = 'disabled'
        next_button_state = 'normal'
        return return_button_state,next_button_state

def middle_button_state():
    return_button_state = 'normal'
    next_button_state = 'normal'
    return return_button_state, next_button_state

def finally_button_state():
    return_button_state = 'normal'
    next_button_state = 'disabled'
    return return_button_state, next_button_state

# def show_information(win,font_code,dict_images):
#     global list1
#     list1 = []
#
#     for i in dict_images:
#         list1.append(i)
#
#     #  [path,path, path, path]
#     for i in range(len(list1)):
#         list_information = dict_images[list1[i]]
#         if i == 0:
#             return_state,next_state = first_button_state()
#             button_all(win,font_code,list_information,return_state,next_state)
#
#         elif  0 < i < len(list1):
#             return_state, next_state = middle_button_state()
#             button_all(win,font_code,list_information,return_state,next_state)
#         elif i == len(list1):
#             return_state, next_state = finally_button_state()
#             button_all(win,font_code,list_information,return_state,next_state)
#
#         image1 = Image.open(list1[i])
#         image1_size = image1.size
#         print(image1_size)
#         print(type(image1_size[0]))
#         if image1_size[0] > image1_size[1]:
#             difference = image1_size[0] - image1_size[1]
#         elif image1_size[1] > image1_size[0]:
#             difference = image1_size[1] - image1_size[0]
#         two = 258 + difference
#         image1.thumbnail((two, 258))
#         ima = ImageTk.PhotoImage(image1)
#         label_code = tkinter.Label(win, font=font_code, image=ima, width=220, height=220)
#         label_code.place(x=150, y=100)

def show_information(win,font_code,dict_images):
    global list1
    list1 = []
    for i in dict_images:
        list1.append(i)

    list_information = dict_images[list1[0]]

    image1 = Image.open(list1[0])
    image1_size = image1.size
    print(image1_size)
    print(type(image1_size[0]))
    if image1_size[0] > image1_size[1]:
        difference = image1_size[0] - image1_size[1]
    elif image1_size[1] > image1_size[0]:
        difference = image1_size[1] - image1_size[0]
    two = 258 + difference
    image1.thumbnail((two, 258))
    ima = ImageTk.PhotoImage(image1)
    label_code = tkinter.Label(win, font=font_code, image=ima, width=220, height=220)
    label_code.place(x=150, y=100)
    base_information(win, font_code, list_information)
    extend_information(win, font_code, list_information)


def show(dict_images):
    win = tkinter.Tk()
    win.title(r"Students's  information show !  ")
    win.geometry('800x600')
    Action(win)
    font_code = ('楷体',15)
    # show_information(win,font_code,dict_images)
    global list1
    list1 = []
    for i in dict_images:
        list1.append(i)

    list_information = dict_images[list1[0]]

    image1 = Image.open(list1[0])
    image1_size = image1.size
    print(image1_size)
    print(type(image1_size[0]))
    if image1_size[0] > image1_size[1]:
        difference = image1_size[0] - image1_size[1]
    elif image1_size[1] > image1_size[0]:
        difference = image1_size[1] - image1_size[0]
    two = 258 + difference
    image1.thumbnail((two, 258))
    ima = ImageTk.PhotoImage(image1)
    label_code = tkinter.Label(win, font=font_code, image=ima, width=220, height=220)
    label_code.place(x=150, y=100)
    base_information(win, font_code, list_information)
    extend_information(win, font_code, list_information)





    # button1 = tkinter.Button(win,text='next', font=('楷体', 15), width=10)
    # button1.place(x=440, y=540)
    # button1 = tkinter.Button(win,text='<----', font=('楷体', 15), width=5,)
    # button1.place(x=5, y=5)

    win.mainloop()
