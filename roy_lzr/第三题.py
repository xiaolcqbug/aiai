# 进程间通信,共同改变一个变量值0, 一个进程+1 ,另一个进程+2 ,分别加十次,停止,打印最终结果
from multiprocessing import Process
a=0

def first(b):
    global a
    for i in range(b):
        a=a+1

def second(c):
    global a
    for i in range(c):
        a=a+2
if __name__ == '__main__':
    p1=Process(target=first,args=(10,))
    p2=Process(target=second,args=(10,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(a)
