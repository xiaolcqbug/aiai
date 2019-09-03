from multiprocessing import Process, Queue
from time import sleep
def run(q):
    a = q.get()
    for i in range(10):
        a += 1
    q.put(a)


def run1(q):
    a = q.get()
    for i in range(10):
        a += 2
    q.put(a)


if __name__ == '__main__':
    q = Queue()
    a = 0
    q.put(a)
    t1 = Process(target=run, args=(q,))
    t2 = Process(target=run, args=(q,))
    t1.start()
    t2.start()
    sleep(3)
    print(q.get())
