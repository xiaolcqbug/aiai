# 进程间通信,共同改变一个变量值0, 一个进程+1 ,另一个进程+2 ,分别加十次,停止,打印最终结果
from multiprocessing import Pool,Queue
a=0
q = Queue(a)
def p1(q):
    h=q.get()
    h+=1
    print('p1:{}'.format(h))
    q.put(h)
def p2(q):
    c=q.get()
    c+=2
    print('p2:{}'.format(c))
    q.put(c)

if __name__ == '__main__':
    g = 0
    while g<11:
        pool = Pool()
        pool.apply_async(func=p1,args=(q,))
        b=q.get()
        pool.apply_async(func=p2,args=(q,))
        pool.close()
        pool.join()
        g+=1
