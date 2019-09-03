# 线程两种写法
from  threading import Thread

# def play(a):
#     for i in range(3):
#         print('它正在玩{}'.format(a))
#
#
# p1=Thread(target=play,args=('什么',))
# p1.start()


class Range_num(Thread):
    def __init__(self,x):
        super(Range_num, self).__init__()
        self.x=x

    def run(self):
        for i in range(self.x):
            print('你在干什么')

p1=Range_num(3,)
p1.start()