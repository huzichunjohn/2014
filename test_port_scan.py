#!/bin/env python
#-*- coding=utf-8 -*-

import sys
import threading
import socket

class scanner(threading.Thread):
    tlist = []
    maxthreads = int(sys.argv[2])
    evnt = threading.Event()
    lck = threading.Lock()

    def __init__(self, tn, host):
        threading.Thread.__init__(self)
        self.threadnum = tn
        self.host = host

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.host, self.theadnum))
            print "%d: successfully connected" % self.threadnum
            s.close()
        except:
            print "%d: connection failed" % self.threadnum

        scanner.lck.acquire()
        scanner.tlist.remove(self)
        print "%d: now active == %s" % self.threadnum, scanner.tlist
        if len(scanner.tlist) == scanner.maxthread - 1:
            scanner.evnt.set()
            scanner.evnt.clear()
        scanner.lck.release()

        def newthread(pn, hst):
            scanner.lck.acquire()
            sc = scanner(pn, hst)
            scanner.lck.release()
            sc.start()
            print "%d: starting check" % pn
            print "%d: now active == %s" % pn, scanner.tlist
        newthread = staticmethod(newthread)


def main():
    host = sys.argv[1]
    for i in range(1, 100):
        scanner.lck.acquire()
        print "%d: attempting check" % i
        if len(scanner.tlist) >= scanner.maxthreads:
            print "%d: need to wait" % i
            scanner.lck.release()
            scanner.evnt.wait()
        else:
            scanner.lck.release()
        scanner.newthread(i, host)
    
    for sc in scanner.tlist:
        sc.join()

if __name__ == "__main__":
    main()




