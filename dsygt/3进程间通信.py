#有两种答案,第一种,结果为20,第二种结果为30
from multiprocessing import Process, Queue
x = 0

#第一种
def sum1():
    global x
    for i in range(1, 11):
        x += 1
        # print('第{}次处理'.format(i))
    print('进程1中的结果:', x)


def sum2():
    global x
    for i in range(1, 11):
        x += 2
    print('进程2中的结果:', x)


if __name__ == '__main__':
    p1 = Process(target=sum1)  # args为元祖!!!
    p1.start()
    p1.join()
    p2 = Process(target=sum2)  # args为元祖!!!
    p2.start()
    p2.join()
    # print('第一种最终结果为:',x)


# //////////////////////第二种,结果为30/////////////////////////////
# from multiprocessing import Process, Queue

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
    print('第二种最终结果为:{}'.format(num))
