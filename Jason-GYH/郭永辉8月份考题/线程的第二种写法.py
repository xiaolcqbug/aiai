from threading import Thread
class MyThread(Thread):
    def __init__(self,food):
        Thread.__init__(self)
        self.food = food
    def run(self):
        print('中午吃{}'.format(self.food))

if __name__ == '__main__':

    t = MyThread('盖浇饭')
    t.start()