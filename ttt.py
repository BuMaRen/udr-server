# import os
import time
# from socketserver import TCPServer, BaseServer, BaseRequestHandler
from threading import Thread, Semaphore

def my_release1(Sema:Semaphore):
    time.sleep(20)
    print('不生产信号量')

def my_release(Sema:Semaphore):
    time.sleep(20)
    print('生产1个信号量')
    Sema.release(1)

sema = Semaphore(0)
t = Thread(target=my_release, args=[sema])
t.start()
t = Thread(target=my_release, args=[sema])
t.start()
t = Thread(target=my_release, args=[sema])
t.start()
t = Thread(target=my_release, args=[sema])
t.start()
t = Thread(target=my_release, args=[sema])
t.start()
t = Thread(target=my_release1, args=[sema])
t.start()

for i in range(6):
    sema.acquire()
    print(f'获取到{i+1}个信号量')

