from multiprocessing import  Process

class MyProcess(Process):
    def __init__(self,food):
        Process.__init__(self)
        self.food = food
    def run(self):
        print('中午吃{}'.format(self.food))

if __name__ == '__main__':

    q = MyProcess('盖浇饭')
    q.start()