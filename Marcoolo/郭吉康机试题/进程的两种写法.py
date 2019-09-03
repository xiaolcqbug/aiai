from multiprocessing import Process
from time import *

def kang():
    for i in range(10, 10000):
        print(i)

def kang2():
    for i in range(0, 100):
        print('-->',i)

if __name__ == '__main__':
    p1 = Process(target = kang, name = 'shu1 ')
    p1.start()

    p2 = Process(target = kang2)
    p2.start()

    sleep(5)

#*************** 第二种 *************************************
from multiprocessing import Process

class Kang(Process):
    def run(self):
        for i in range(0, 10):
            print('i:', i)


if __name__ == '__main__':    # 格式

    p1 = Kang()
    p1.start()
    p1.run()








