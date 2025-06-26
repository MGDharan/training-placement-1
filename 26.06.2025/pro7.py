from threading import Thread, Lock
import time, random

buffer = []
lock = Lock()

def producer():
    while True:
        item = random.randint(1, 100)
        lock.acquire()
        buffer.append(item)
        print(f"Produced: {item}")
        lock.release()
        time.sleep(1)

def consumer():
    while True:
        lock.acquire()
        if buffer:
            item = buffer.pop(0)
            print(f"Consumed: {item}")
        lock.release()
        time.sleep(2)

Thread(target=producer).start()
Thread(target=consumer).start()
