from multiprocessing import Process
from multiprocessing import Queue
from time import sleep
a=0

def task1(q):
    global a
    q.put(10)
    for a in range(10):
        a = a + 1
        print('--', a)



def task2(q):
    global a

    for a in range(10):
        a = a + 2
        print('--', a)
    q.put(10)


if __name__ == '__main__':
    q=Queue(maxsize=10)
    # print(q.get(block=False))
    # print(q.get())
    p1=Process(target=task1,args=(q,))
    p1.start()
    p1.join()
    print(q.get(block=False))
    p2=Process(target=task2,args=(q,))
    p2.start()
    # p2.join()
    print(q.get())
    # print(a.bit_length())
    # p2.join()
    # while 1:
    #     print(q.get())

