#!/bin/env python
#-*- coding=utf-8 -*-

from Queue import Queue
import concurrent.futures
import random
import time

q = Queue()
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def worker(x):
    if random.randint(0, 1):
        time.sleep(0.1)

    result = x * x 
    q.put(result)

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for num in l:
            executor.submit(worker, num)

    while not q.empty():
        print q.get()

if __name__ == "__main__":
    main()















































