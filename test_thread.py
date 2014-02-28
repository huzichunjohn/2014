#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-2-27
# Version: 1.0

import time
import thread

def worker(i, interval):
    while True:
        current_time = get_current_time()
        print "[ " + current_time + " ]" + " Thread " + str(i) + " " + str(interval)
        time.sleep(interval)

def main(times):
    for i in range(times):
        print i
        thread.start_new_thread(worker, (i, (i*2 + 1)))

def get_current_time():
    """Get current time."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

def get_millisecond(time):
    item = time.split(":")
    sum = (int(item[0])*3600 + int(item[1])*60 + int(item[2]))*1000 + int(item[3])
    return sum

if __name__ == '__main__':
    print "Start ......"
    main(5)
    time.sleep(25)
    print "Stop ......"

