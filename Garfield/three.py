# 进程间通信,共同改变一个变量值0, 一个进程+1 ,另一个进程+2 ,分别加十次,停止,打印最终结果
from multiprocessing import Process, Queue


def task1(x, q):
    for i in range(10):
        x += 1
    q.put(x)


def task2(q):
    x = q.get()
    for i in range(10):
        x += 2
    print(x)


if __name__ == '__main__':
    x = 0
    q1 = Queue()
    p1 = Process(target=task1, args=(x, q1))
    p2 = Process(target=task2, args=(q1,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(x)
