
from threading import Thread

def k1(n):
    for i in range(n):
        print('hello python')

if __name__ == '__main__':

    kk = Thread(target=k1,args=(6,))
    kk.start()

#********** 第二种 *********************************

from threading import Thread

class Kang1(Thread):
    def __init__(self,play):
        Thread.__init__(self)
        self.play = play

    def run(self):
        print('玩...{}'.format(self.play))

if __name__ == '__main__':

    k2 = Kang1('单纯')
    k2.start()


















