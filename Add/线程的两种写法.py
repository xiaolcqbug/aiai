from threading import Thread

# def task(a):
#     for n in range(10):
#         print(n,a)
#
#
# if __name__ == '__main__':
#     t1=Thread(target=task,args=(10,))
#     t1.start()

class _Thread(Thread):
    def __init__(self,name,n):
        super(_Thread, self).__init__()
        self.name=name
        self.n=n

    def run(self):
        for n in range(10):
            print('{}是第{}个人..'.format(self.name,self.n))

if __name__ == '__main__':
    t1=_Thread('小花',10)
    t1.start()

