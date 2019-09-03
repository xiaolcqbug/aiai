from multiprocessing import Process
from multiprocessing import Queue
def fun1(q):
    for i in range(10):
        a = q.get()
        a += 1
        q.put(a)
def fun2(q):
    for i in range(10):
        a = q.get()
        a += 2
        q.put(a)
if __name__ == '__main__':
    a = 0
    q = Queue()
    q.put(a)
    p1 = Process(target=fun1, args=(q,))
    p2 = Process(target=fun2, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(q.get())