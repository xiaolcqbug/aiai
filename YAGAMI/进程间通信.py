from multiprocessing import Process
a = 0
def task1():
    global a
    for i in range(10):
        i += 1
        a += 1
    print(a)


def task2():
    global a
    for i in range(10):
        i += 1
        a += 2
    print(a)

if __name__ == '__main__':
    p1 = Process(target=task1)
    p1.start()
    p2 = Process(target=task2)
    p2.start()

