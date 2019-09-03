from multiprocessing import Process, Queue


def add_1(q):
    num = q.get(False)
    for i in range(10):
        num += 1
    q.put(num)


def add_2(q):
    num = q.get()
    for i in range(10):
        num += 2
    q.put(num)


if __name__ == '__main__':
    q = Queue()
    num = 0
    q.put(num)
    p1 = Process(target=add_1, args=(q,))
    p1.start()
    p1.join()
    p2 = Process(target=add_2, args=(q,))
    p2.start()
    p2.join()
    num = q.get()
    print('num的最终结果为:{}'.format(num))
