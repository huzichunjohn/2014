#!/bin/env python
#-*- coding=utf-8 -*-
"""Just for python study."""
import sys
import thread
import socket
import time
import logging

def get_ip(name):
    """Get ip from domain name."""
    logging.info('[%s]: %s', name, socket.gethostbyname(name))

def get_domain_infos(filename):
    """Get domain infos."""
    domains = []
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        for line in lines:
            domains.append(line.strip())
        return domains
    except IOError:
        logging.debug("Open file failed.")
        sys.exit(1)
    finally:
        f.close()

def main():
    """Start to run."""
    hostname = get_domain_infos('name.txt')
    logging.debug(hostname)
    length = len(hostname)

    for i in range(length):
        thread.start_new_thread(get_ip, (hostname[i],))

if __name__ == "__main__":
    logging.basicConfig(filename='domain.log', \
                        format='[%(asctime)s] %(message)s', \
                        datefmt='%Y-%m-%d %I:%M:%S %p', level=logging.DEBUG)
    main()
    time.sleep(5)
