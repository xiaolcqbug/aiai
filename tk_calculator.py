from tkinter import *
from functools import reduce

get1 = 0
get2 = 0


class Counter:  # 计算器

    save1 = []  # 保存
    result = 0  # 结果

    def __init__(self, click):  # 点击
        self.click = click

    @classmethod
    def change(cls, list1):  # [str] -->float
        str1 = ''
        for i in list1:
            str1 += i
        return float(str1)

    def record(self, event):  # 记录
        global res1, get1
        Counter.save1.append(self.click)
        print(Counter.save1)

        if Counter.save1[-1] in ['+', '-', '*', '/', '%', '//']:
            res1 = Counter.save1.pop()
            if len(Counter.save1) > 1:
                copy1 = Counter.save1
                if Counter.save1.count('.') == 0:
                    get1 = reduce(lambda x, y: int(x) * 10 + int(y), copy1)
                else:
                    get1 = Counter.change(copy1)
            else:
                if Counter.save1 != []:
                    get1 = int(Counter.save1[0])
                    print('get1-->', get1)
                else:
                    pass

            Counter.save1.clear()

        label1['text'] = Counter.save1

    def step_back(self, event):  # 退格
        if Counter.save1 == []:
            pass
        else:
            Counter.save1.pop()
            label1['text'] = Counter.save1

    def clear_all(self, event):  # 清空全部
        Counter.save1.clear()
        label1['text'] = Counter.save1

    def clear_get2(self, event):  # 清空 第二次输入
        Counter.save1.clear()
        label1['text'] = get1

    def decimal(self, event):  # 小数点
        if Counter.save1.count('.') >= 1:
            pass
        else:
            if Counter.save1 == []:
                Counter.save1.append('0')
            Counter.save1.append('.')
            label1['text'] = Counter.save1

    def operation(self, event):
        global get2
        if get1 != 0 or get2 != 0:
            if Counter.save1 != []:
                if len(Counter.save1) > 1:
                    if Counter.save1.count('.') == 0:
                        get2 = reduce(lambda x, y: int(x) * 10 + int(y), Counter.save1)
                    else:
                        get2 = Counter.change(Counter.save1)
                        print('get-->', get2)
                else:
                    get2 = int(Counter.save1[0])
                    print('get2-->', get2)

                Counter.fun1()

            else:
                if res1 == 'x%':
                    Counter.result = get1 / 100
                    label1['text'] = Counter.result
                    Counter.save1.clear()
                    Counter.save1.append(Counter.result)

        else:
            pass

    @classmethod
    def fun1(cls):
        print('=', get1, get2)
        if res1 == '+':
            Counter.result = get1 + get2

        elif res1 == '-':
            Counter.result = get1 - get2

        elif res1 == '*':
            Counter.result = get1 * get2

        elif res1 == '//':
            Counter.result = get1 // get2

        elif res1 == '%':
            Counter.result = get1 % get2

        else:
            Counter.result = get1 / get2

        label1['text'] = Counter.result
        Counter.save1.clear()
        Counter.save1.append(Counter.result)


def menu_command():
    label1['text'] = 'I am a counter menu'


win = Tk()
win.title('计算器')
win.maxsize(220, 190)
win.resizable(0, 0)  # 禁止最大化

m1 = Menu(win)  # 下拉菜单
checkmenu = Menu(m1)
editmenu = Menu(m1)
helpmenu = Menu(m1)
for i in ['复制', '粘贴', ]:
    editmenu.add_command(label=i, command=menu_command)
for i in ['帮助', '关于计算器', ]:
    helpmenu.add_command(label=i, command=menu_command)
m1.add_cascade(label='查看', menu=checkmenu)
m1.add_cascade(label='编辑', menu=editmenu)
m1.add_cascade(label='帮助', menu=helpmenu)
win['menu'] = m1

label1 = Label(master=win, width=32, height=2, bg='#00ffff')  # 显示屏
label1.grid(row=1, column=0, columnspan=5)

names = locals()


def button(n, text, row, column, width=5, height=None, columnspan=None, rowspan=None):
    names['button{}'.format(n)] = Button(win, text=text, width=width, height=height)
    names['button{}'.format(n)].grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)


list1 = ['退格', 'CE', 'C', '', '%', '7', '8', '9', '/', 'x%', '4', '5', '6', '*', '//', '1', '2', '3', '-', '=', '0',
         '.',
         '+']
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

for i in range(2, 7):
    for x in range(0, 5):
        for a in list1:
            for n in list2:
                if a == '0':
                    button(22, a, i, x, width=12, columnspan=2)
                    list1.remove(a)
                    break
                elif a == '=':
                    button(23, a, i, x, height=3, rowspan=2)
                    list1.remove(a)
                    break
                elif i == 6 and (x == 1 or x == 4):
                    continue

                else:
                    button(n, a, i, x)
                    list1.remove(a)
                    list2.remove(n)
                    break
            break

button1.bind('<Button-1>', Counter('<-').step_back)
button2.bind('<Button-1>', Counter('CE').clear_get2)
button3.bind('<Button-1>', Counter('C').clear_all)
button5.bind('<Button-1>', Counter('%').record)
button6.bind('<Button-1>', Counter('7').record)
button7.bind('<Button-1>', Counter('8').record)
button8.bind('<Button-1>', Counter('9').record)
button9.bind('<Button-1>', Counter('/').record)
button10.bind('<Button-1>', Counter('x%').record)
button11.bind('<Button-1>', Counter('4').record)
button12.bind('<Button-1>', Counter('5').record)
button13.bind('<Button-1>', Counter('6').record)
button14.bind('<Button-1>', Counter('*').record)
button15.bind('<Button-1>', Counter('//').record)
button16.bind('<Button-1>', Counter('1').record)
button17.bind('<Button-1>', Counter('2').record)
button18.bind('<Button-1>', Counter('3').record)
button19.bind('<Button-1>', Counter('-').record)
button20.bind('<Button-1>', Counter('.').decimal)
button21.bind('<Button-1>', Counter('+').record)
button22.bind('<Button-1>', Counter('0').record)
button23.bind('<Button-1>', Counter('=').operation)

win.mainloop()
