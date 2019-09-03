from threading import Thread
class Task(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        print('哈哈')
if __name__ == '__main__':
    p1 = Task()
    p2 = Task()
    p1.start()
    p2.start()