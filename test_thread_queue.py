#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-2-28
# Version: 1.0

from Queue import Queue
import threading
import time
import random
import logging

class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(20):
            logging.debug(self.getName() + ": add " + str(i) + " to queue.")
            self.data.put(i)
            time.sleep(random.randrange(10)/10.0)
        logging.debug(self.getName() + ": finish.")

class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(20):
            logging.debug(self.getName() + ": get " + str(self.data.get()) + " from queue.")
            time.sleep(random.randrange(10)/10.0)
        logging.debug(self.getName() + ": finish.")

def main():
    queue = Queue()
    producer = Producer('producer', queue)
    consumer = Consumer('consumer', queue)

    logging.debug("start thread ......")
    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    
    logging.debug("all threads have finished.")


if __name__ == "__main__":
    logging.basicConfig(filename='queue.log', format="[%(asctime)s] (%(threadName)10s) %(message)s", datefmt="%Y-%m-%d %I:%M:%S %p", level=logging.DEBUG)  
    main()











































