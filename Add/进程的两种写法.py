from multiprocessing import Process

# def task(n):
#     for n in range(1,6):
#         print('--',n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(6,))
#     p1.start()

class _Process(Process):
    def __init__(self,name,food):
        super(_Process, self).__init__()
        self.name=name
        self.food=food

    def run(self):
        print('{}在偷偷的{}'.format(self.name,self.food))

if __name__ == '__main__':
    p1=_Process('小明','吃蛋糕')
    p1.start()