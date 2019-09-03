from threading import Thread
def task1(q):
    print('晚上吃{}'.format(q))
if __name__ == '__main__':
    t = Thread(target=task1,args=('饺子',))
    t.start()