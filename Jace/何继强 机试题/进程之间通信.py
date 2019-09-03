from multiprocessing import Process, Queue


def task1(a, q):
    for i in range(10):
        a += 1
    q.put(a)


def task2(q):
    a = q.get()
    for i in range(10):
        a += 2
    print(a)


if __name__ == '__main__':
    a = 0
    q = Queue()
    p1 = Process(target=task1, args=(a, q))
    p2 = Process(target=task2, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(a)