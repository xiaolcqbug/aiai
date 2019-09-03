from threading import Thread
# def task1(where):
#     print('小明在{}学习...'.format(where))
# if __name__=='__main__':
#     t=Thread(target=task1,args=('教室',))
#     t.start()


class MyThread(Thread):
    def __init__(self,where):
        super(MyThread, self).__init__()
        self.where=where
    def run(self):
        print('小明在{}学习...'.format(self.where))
if __name__=='__main__':
    t1=MyThread('教室')
    t1.start()
