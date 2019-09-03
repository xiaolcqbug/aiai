# 进程两种写法

from multiprocessing import Process

# def play(a):
#     for i in range(3):
#         print('它正在玩{}'.format(a))
# 
# if __name__ == '__main__':
#     p1=Process(target=play,args=('什么',))
#     p1.start()


class Range_num(Process):
    def __init__(self,x):
        super(Range_num, self).__init__()
        self.x=x

    def run(self):
        for i in range(self.x):
            print('你在干什么')
if __name__ == '__main__':
    p1=Range_num(3,)
    p1.start()