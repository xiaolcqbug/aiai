#��һ��
from threading import Thread

# def task1(food):
#     print('�Է�...{}'.format(food))
# if __name__ == '__main__':
#     t = Thread(target=task1,args=('����',))
#     t.start()

# �ڶ���
class Count1(Thread):
    def __init__(self,two1):
        super(Count1, self).__init__()
        self.two1 = two1
    def run(self):
        print('runing task',self.two1)

p1 = Count1(1)
p1.start()
