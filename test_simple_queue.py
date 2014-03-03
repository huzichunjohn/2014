#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-3-3
# Version: 1.0

import Queue


if __name__ == "__main__":
    queue = Queue.Queue(6)
    for i in range(5):
        queue.put(i)
    queue.put((1,2,3))
    print queue.full()

    while not queue.empty():
        print queue.get()

    lifo = Queue.LifoQueue()
    for i in range(5):
        lifo.put(i)

    print lifo.get()


