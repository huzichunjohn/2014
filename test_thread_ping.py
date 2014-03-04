#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-3-4
# Version: 1.0

import os
import re
import threading

#received_packages = re.compile(r"(\d) received")
#status = ("no response", "alive but losses", "alive")
#
#for suffix in range(20, 30):
#    ip = "58.63.236." + str(suffix)
#    ping_out = os.popen("ping -q -c2 " + ip, "r")
#    print "... pinging ", ip
#    lines = ping_out.readlines()
#    for line in lines:
#        n_received = received_packages.findall(line)
#        if n_received:
#            print ip + ": " + status[int(n_received[0])]

class IP_Check(threading.Thread):
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = ip
        self.__successful_pings = -1

    def run(self):
        ping_out = os.popen("ping -q -c2 " + self.ip, "r")
        while True:
            line = ping_out.readline()
            if not line:
                break
            n_received = re.findall(received_packages, line)
            if n_received:
                self.__successful_pings = int(n_received[0])
    
    def status(self):
        if self.__successful_pings == 0:
            return "no response"
        elif self.__successful_pings == 1:
            return "alive, but 50% package loss"
        elif self.__successful_pings == 2:
            return "alive"
        else:
            return "shouldn't occur"

received_packages = re.compile(r"(\d) received")

check_results = []
for suffix in range(24, 90):
    ip = "58.63.236." + str(suffix)
    current = IP_Check(ip)
    check_results.append(current)
    current.start()

for el in check_results:
    el.join()
    print "Status from", el.ip, "is", el.status()


















































