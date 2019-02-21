# coding:utf8
import threading
import time

p_list = []
num = 0 
def run(n):
    semaphore.acquire()
    time.sleep(1)
    print ('this is %s num' % n)
    semaphore.release()


lock = threading.Lock()
print(lock.acquire())



print (num)