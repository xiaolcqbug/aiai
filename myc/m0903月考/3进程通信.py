# 进程间通信,共同改变一个变量值0, 一个进程+1 ,另一个进程+2 ,分别加十次,停止,打印最终结果
from multiprocessing import Process
from multiprocessing import Queue

def process1(q):
    for i in range(10):
        a = q.get()
        a += 1
        q.put(a)

def process2(q):
    for i in range(10):
        a = q.get()
        a += 2
        q.put(a)

if __name__ == '__main__':
    a = 0
    q = Queue()
    q.put(a)
    p1 = Process(target=process1, args=(q,))
    p2 = Process(target=process2, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print( q.get())