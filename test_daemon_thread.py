#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-2-28
# Version: 1.0

import time
import threading
import logging

class MyDaemonThread(threading.Thread):
    id = 1
    data = []

    def __init__(self, interval=1):
        threading.Thread.__init__(self)
        self.__interval = interval
        self.id = MyDaemonThread.getID()
        self.__stop = False

    def run(self):
        count = 0
        while count < 10 and not self.__stop:
            logging.debug("ID: %d, sleep %d, current time is: %s", self.id, self.__interval, time.ctime())
            time.sleep(self.__interval)
            count += 1
            self.data.append(count)
        else:
            logging.debug("ID %d is over.", self.id)

    @staticmethod
    def getID():
        MyDaemonThread.id += 1
        return MyDaemonThread.id

    def stop(self):
        self.__stop = True

if __name__ == "__main__":
    logging.basicConfig(filename='daemon.log', format='[%(asctime)s] (%(threadName)10s) %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p', level=logging.DEBUG)
    logging.debug("Start main thread ......")
    mydaemon = MyDaemonThread(3)
    mydaemon.setDaemon(True)
    mydaemon.start()
    logging.debug("Stop main thread ......")
    time.sleep(15)
    mydaemon.stop()
