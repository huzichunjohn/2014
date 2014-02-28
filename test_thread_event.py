#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-2-28
# Version: 1.0

import time
import threading
import logging

class MyThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self, name=thread_name)

    def run(self):
        global event
        if event.isSet():
            #event.clear()
            #event.wait()
            logging.debug("start to execute. [1]")
            print self.getName()
            time.sleep(2)
            #event.set()
            logging.debug("stop to execute. [1]")
        else:
            #event.set()
            #event.wait()
            logging.debug("start to execute. [2]")
            print self.getName()
            time.sleep(2)
            #event.clear()
            logging.debug("stop to execute. [2]")

if __name__ == "__main__":
    logging.basicConfig(filename="event.log", format='[%(asctime)s] (%(threadName)10s) %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p', level=logging.DEBUG)
    event = threading.Event()
    event.set()

    threads = []
    for i in range(10):
        thread = MyThread(str(i))
        threads.append(thread)

    for thread in threads:
        thread.start()
    
#    for thread in threads:
#        thread.join()

