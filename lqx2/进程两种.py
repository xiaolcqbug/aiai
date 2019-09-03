from multiprocessing import Process

# def nim():
#     for i in range(5):
#         print(i)
# if __name__ == '__main__':
#     n1 = Process(target = nim)
#     n1.start()


class Myprocess(Process):
    def __init__(self,x,y):
        Process.__init__(self)
        self.x = x
        self.y = y
    def run(self):
        for i in range(self.x,self.y):
            print(i)
if __name__ == '__main__':
    m1 = Myprocess(2,6)
    m1.start()