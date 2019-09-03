from multiprocessing import Process
from multiprocessing import Queue
from time import *
def task1(a):
    b = a.get()
    for i in range(10):
        b += 1
    a.put(b)



def task2(a):
    b = a.get()
    for i in range(10):
        b += 2
    a.put(b)



if __name__ == '__main__':
    b = 0
    a = Queue()
    a.put(b)
    p1 = Process(target=task1, args=(a,))
    p2 = Process(target=task2, args=(a,))
    p1.start()
    p2.start()
    sleep(2)
    print(a.get())