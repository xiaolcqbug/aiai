from multiprocessing import  Process

def task1(q):
    print('晚上吃{}'.format(q))
if __name__ == '__main__':
    q = Process(target=task1,args=('饺子',))
    q.start()