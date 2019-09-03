from multiprocessing import Process

class Myprocess(Process):
    def __init__(self):
        super().__init__()
    def run(self):
        print('哈哈')
if __name__ == '__main__':
    p=Myprocess()
    p1=Myprocess()
    p.start()
    p1.start()
    print('主')