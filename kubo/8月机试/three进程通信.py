# 进程间通信,共同改变一个变量值0,
# 一个进程+1 ,另一个进程+2 ,分别加十次,停止,打印最终结果
from multiprocessing import Process
from multiprocessing import Queue

sum1 = 0
q = Queue()
q.put(sum1)


def task1(q):
    b = q.get()
    b = b+1
    q.put(b)

def task2(q):
    b = q.get()
    b = b+2
    q.put(b)


if __name__ == '__main__':
    for i in range(1, 11):
        p1 = Process(target=task1,args=(q,))
        p2 = Process(target=task2,args=(q,))
        p1.start()
        p1.join()
        sum1 =q.get()
        q.put(sum1)
        p2.start()
        p2.join()
        sum1 =q.get()
        q.put(sum1)
        print(sum1)


