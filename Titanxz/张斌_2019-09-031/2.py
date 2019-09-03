#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/9/3 14:43:01
# @License :   (C) Copyright 2019, {python_1904}

# 线程两种写法

# 第一种写法(函数)

from threading import Thread

def run(arg):
    print('hellp {}'.format(arg))

if __name__ == '__main__':
    p = Thread(target=run, args=('word',))
    p.start()


# 第二种写法(继承Thread类的线程)

from threading import Thread

class MyThread(Thread):
    def __init__(self,arg):
        # super(MyThread, self).__init__()
        Thread.__init__(self)
        self.arg = arg

    def run(self):
        print('hello {}'.format(self.arg))

if __name__ == '__main__':
    p1 = MyThread('word')
    p1.start()

