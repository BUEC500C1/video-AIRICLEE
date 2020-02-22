import time
import queue
import threading
from getTwits import *

def worker(i):
    while True:
        item = q.get()
        if item is None:
            print("Thread %s find the object None, now it can take a rest ^-^" % i)
            break

        # execute do_work(item)
        time.sleep(0.5)
        getResult(item)
        print("Thread %s hava finished the task <%s> ！" % (i, item))
        
        # After finish this task, return the signal
        q.task_done()


if __name__ == '__main__':
    num_of_threads = 3

    source = ['Jackson', 'Vincent', 'Lee', 'EC_500_Staff', 'Osama', 'TA', 'Admin']

    # create queue
    q = queue.Queue()
    
    # build threads pool
    threads = []
    
    # create thread, and put them into pools
    for i in range(1, num_of_threads+1):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.daemon = True
        t.start()

    # put the task into queue
    for item in source:
        time.sleep(0.5)
        q.put(item)


    q.join()
    print("-----All the task have been finished-----")
    for i in range(num_of_threads):
        q.put(None)
    for t in threads:
        t.join()
