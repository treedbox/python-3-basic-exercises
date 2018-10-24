import threading
import time
from queue import Queue


print_lock = threading.Lock()


def job(worker):
    time.sleep(.5)

    with print_lock:
        print(threading.current_thread().name, worker)


def threader():
    while True:
        worker = q.get()
        job(worker)
        q.task_done()


q = Queue()

for x in range(10):  # 10 threads
    t = threading.Thread(target=threader)
    t.daemon = True  # die when the main thread dies
    t.start()


start = time.time()


for worker in range(20):
    q.put(worker)


q.join()

print('Entire job took:', time.time() - start)
