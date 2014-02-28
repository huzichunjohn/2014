#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-2-28
# Version: 1.0

import threading
import time

def worker(time):
    for i in range(time):
        print "[ Thread %s ]: %s." % (threading.currentThread().getName(), i+1)

def main(thread_number):
    threads = []
    for i in range(thread_number):
        threads.append(threading.Thread(target=worker, name="worker"+str(i+1), args=(3,)))

    for i in threads:
        i.start()

    for i in threads:
        i.join()


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
        print "init thread " + self.getName()
    
    def run(self):
        print "start to run " + self.getName()
        for i in range(self.num):
            print "[ Thread %s ]: %s." % (self.getName(), i+1)
            
if __name__ == "__main__":
    for i in range(3):
        t = MyThread(3)
        t.start()
        t.join
        # you can see that the threads is not concurrent.
        time.sleep(5) 












































