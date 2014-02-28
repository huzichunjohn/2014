#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-2-28
# Version: 1.0

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,thread_name):
        super(MyThread, self).__init__(name=thread_name)

    def run(self):
        global sum
        #print "before: thread %s, sum [ %d ]" % (threading.currentThread().getName(), sum)
        for i in range(4):
            sum += i
        #print "thread %s, sum [ %d ]" % (threading.currentThread().getName(), sum)
        time.sleep(0.1)
        #print "after: thread %s, sum [ %d ]" % (threading.currentThread().getName(), sum)
        print sum
    
if __name__ == "__main__":
    threads = []
    for i in range(10):
        thread = MyThread(str(i))
        threads.append(thread)

    sum = 0
    for i in threads:
        i.start()

    for i in threads:
        i.join()
