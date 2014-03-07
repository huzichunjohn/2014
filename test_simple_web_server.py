#!/bin/env python
#-*- coding=utf-8 -*-
import sys
import socket
import time
import threading
import gevent

def worker(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        handle_request(cli, time.sleep)

def handle_request(s, sleep):
    try:
        s.recv(1024)
        sleep(0.1)
        s.send('''HTTP/1.0 200 OK\r\n\r\nHello world.\r\n''')
        s.shutdown(socket.SHUT_WR)
        print '.',
    except Exception, e:
        print "e", e
    finally:
        sys.stdout.flush()
        s.close()

def threads(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        t = threading.Thread(target=handle_request, args=(cli, time.sleep))
        t.daemon = True
        t.start()

def greenlet(port):
    from gevent import socket
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli, gevent.sleep)




if __name__ == "__main__":
    #worker(int(sys.argv[1]))
    #threads(int(sys.argv[1]))
    greenlet(int(sys.argv[1]))














































