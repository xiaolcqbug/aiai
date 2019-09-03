#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/9/3 14:43:08
# @License :   (C) Copyright 2019, {python_1904}


# 进程间通信,共同改变一个变量值0, 一个进程+1 ,另一个进程+2 ,
# 分别加十次,停止,打印最终结果

from multiprocessing import Process

num = 0

def add_one():
    global num
    for n in range(10):
        num += 1
    print(num)


def add_two():
    global num
    for n in range(10):
       num +=  2
    print(num)


if __name__ == '__main__':
    p1 = Process(target=add_one)
    p2 = Process(target=add_two)
    p1.start()
    p2.start()

















