from multiprocessing import Process
from multiprocessing import Queue

def task1(b):
    for i in range(10):
        a = b.get()
        a = a + 1
        b.put(a)


def task2(b):
    for i in range(10):
        a = b.get()
        a = a + 2
        b.put(a)

if __name__ == '__main__':
    a = 0
    b = Queue()
    b.put(a)
    p1 = Process(target=task1, args=(b,))
    p1.start()
    p2 = Process(target=task2, args=(b,))
    p2.start()
    p1.join()
    p2.join()
    print(b.get())