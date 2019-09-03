from threading import Thread
def task():
    print('哈哈')
if __name__ == '__main__':
    p = Thread(target=task)
    p.start()