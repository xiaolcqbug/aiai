from multiprocessing import Process
# def shushu(a,b):
#     for i in range(a,b):
#         print(i)
# if __name__=='__main__':
#     p1=Process(target=shushu,args=(1,10))
#     p1.start()


class Myprocess(Process):
    def __init__(self,a,b):
        super(Myprocess, self).__init__()
        self.a=a
        self.b=b
    def run(self):
        for i in range(self.a,self.b):
            print(i)
if __name__=='__main__':
    p1=Myprocess(1,5)
    p1.start()