#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-2-27
# Version: 1.0

import logging
import threading
import time

def worker():
    logging.debug('worker start: %s'%time.time())
    time.sleep(2)
    logging.debug('worker stop: %s'%time.time())

def caller():
    logging.debug('caller start: %s'%time.time())
    time.sleep(2)
    worker()
    logging.debug('caller stop: %s'%time.time())

def main():
    caller1 = threading.Thread(target=caller, name='caller')
    worker1 = threading.Thread(target=worker, name='worker')
    worker2 = threading.Thread(target=worker)
    caller1.start()
    worker1.start()
    worker2.start()


if __name__ == "__main__":
    logging.basicConfig(filename='example.log', format='[%(asctime)s] (%(threadName)10s) %(message)s', datefmt='%Y-%m-%d %I:%M:%S.%f %p', level=logging.DEBUG)
    main()


