#!/bin/env python
#-*- coding=utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import Queue
import threading
import urllib2
import time
from BeautifulSoup import BeautifulSoup

hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com",
        "http://ibm.com", "http://apple.com", "http://www.sina.com.cn",
        "http://www.qq.com", "http://www.sohu.com", "http://www.youku.com",
        "http://www.iqiyi.com"]

queue = Queue.Queue()
out_queue = Queue.Queue()

class ThreadUrl(threading.Thread):
    def __init__(self, queue, out_queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
            host = self.queue.get()
            url = urllib2.urlopen(host)
            chunk = url.read()
            self.out_queue.put(chunk)
            self.queue.task_done()

class DatamineThread(threading.Thread):
    def __init__(self, out_queue):
        threading.Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        while True:
            chunk = self.out_queue.get()
            soup = BeautifulSoup(chunk)
            print soup.findAll(['title'])
            self.out_queue.task_done()


start = time.time()
def main():
    for i in range(5):
        t = ThreadUrl(queue, out_queue)
        t.setDaemon(True)
        t.start()

    for host in hosts:
        queue.put(host)

    for i in range(5):
        dt = DatamineThread(out_queue)
        dt.setDaemon(True)
        dt.start()

    queue.join()
    out_queue.join()

main()
print "Elapsed Time: %s" % (time.time() - start)

