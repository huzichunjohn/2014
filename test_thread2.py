#!/bin/env python
#-*- coding=utf-8 -*-

import sys
import thread
import socket
import time
import logging

def get_ip(name, lock):
    logging.info('[%s]: %s' % (name,socket.gethostbyname(name)))
    lock.release()

def get_domain_infos(filename):
    domains = []
    try:
        fp = open(filename, 'r')
        lines = fp.readlines()
        for line in lines:
            domains.append(line.strip())
        return domains
    except:
        logging.debug("Open file failed.")
        sys.exit(1)
    finally:
        fp.close()

def main():
    hostname = get_domain_infos('name.txt')
    logging.debug(hostname)
    length = len(hostname)
    locks = []

    for i in range(length):
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in range(length):
        thread.start_new_thread(get_ip, (hostname[i],locks[i]))

    for i in range(length):
        while locks[i].locked():
           time.sleep(1)

if __name__ == "__main__":
    logging.basicConfig(filename='domain.log', format='[%(asctime)s] %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p', level=logging.DEBUG)
    main()
