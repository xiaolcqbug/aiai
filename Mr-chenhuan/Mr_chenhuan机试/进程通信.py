from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue
from time import *
a = 0
def target1():
    global a
    for i in range(10):
        a += 1
        # q.put(a)
        # sleep(1)
    print(a)

def target2():
    global a
    for i in range(10):
        # n = q.get()
        a += 2
        # q.put(a)
        # sleep(1)
    print(a)


if __name__ == '__main__':
    # p1 = Pool()
    # p1.apply_async(target1)
    # p1.apply_async(target2)
    # p1.close()
    # p1.join()

    p11 = Process(target=target1)
    p12 = Process(target=target2)
    p11.start()
    p12.start()
    # q = Queue()
    # p1 = Process(target=target1,args=(q,))
    # p2 = Process(target=target2,args=(q,))
    # p1.start()
    # p2.start()
