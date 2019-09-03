#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/9/3 14:42:43
# @License :   (C) Copyright 2019, {python_1904}

# 进程两种写法

# 第一种写法(函数)

from multiprocessing import Process

def run(arg):
    print('hellp {}'.format(arg))

if __name__ == '__main__':
    p = Process(target=run, args=('word',))
    p.start()


# 第二种写法(继承Process类的进程)

from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,arg):
        Process.__init__(self)
        self.arg = arg

    def run(self):
        print('hello {}'.format(self.arg))

if __name__ == '__main__':
    p1 = MyProcess('word')
    p1.start()
























