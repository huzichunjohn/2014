#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-3-3
# Version: 1.0

import threading
import Queue
import logging
import time
import random
import sys

queue = Queue.Queue()

class Producer(threading.Thread):
    def __init__(self, thread_name, queue):
        threading.Thread.__init__(self, name=thread_name)
        self._stop = False
        self.queue = queue

    def run(self):
        while not self._stop:
            self.queue.put(self.getName())
            time.sleep(random.randint(1, 10))
            logging.debug(self.getName() + ' put ' + self.getName() + ' to the queue.')
        logging.debug(self.getName() + ' is ready to exit.')

    def stop(self):
        self._stop = True
        logging.debug('[producer exit]' + str(self.isAlive()))

class Consumer(threading.Thread):
    def __init__(self, thread_name, queue):
        threading.Thread.__init__(self, name=thread_name)
        self._stop = False
        self.queue = queue

    def run(self):
        while not self.queue.empty() and not self._stop:
            logging.debug(self.getName() + ' get ' +  self.queue.get() + ' from the queue.')
            time.sleep(random.randint(1,10))
        logging.debug(self.getName() + ' is ready to exit.')

    def stop(self):
        self._stop = True
        logging.debug('[consumer exit]' + str(self.isAlive()))

def main():
    try:
        producers = []
        consumers = []
        for i in range(10):
            p = Producer('Producer' + str(i), queue)
            p.setDaemon(True)
            producers.append(p)

        for i in range(3):
            c = Consumer('Consumer' + str(i), queue)
            c.setDaemon(True)
            consumers.append(c)

        for producer in producers:
            producer.start()

        for consumer in consumers:
            consumer.start()
        
        while True:
            time.sleep(5)
            print "5 seconds gone ......"
    except KeyboardInterrupt:
        print "The program is ready to exit."
        for producer in producers:
            if producer.isAlive():
                logging.debug(producer.getName() + ' is alive')
                producer.stop()
                logging.debug(producer.getName() + ": " + str(producer.isAlive()))
        
        for consumer in consumers:
            if consumer.isAlive():
                logging.debug(consumer.getName() + " is alive.")
                consumer.stop()
                logging.debug(consumer.getName() + ": " + str(consumer.isAlive()))

        for producer in producers:
            producer.join()
        print "Producers finished."

        for consumer in consumers:
            consumer.join()
        print "Consumers finished."
        
        for producer in producers:
            logging.debug(producer.getName() + ": " + str(producer.isAlive()))

        for consumer in consumers:
            logging.debug(consumer.getName() + ": " + str(consumer.isAlive()))

        print "The program is over."

if __name__ == "__main__":
    logging.basicConfig(filename='producer_consumer.log', \
                        format='[%(asctime)s] (%(threadName)10s) %(message)s', \
                        datefmt='%Y-%m-%d %I:%M:%S %p', level=logging.DEBUG)
    main()
