#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-3-3
# Version: 1.0

import threading

def hello(name):
    print "hello " + name

def set_interval(sec, func, *args, **kw):
    def wrapper():
        set_interval(sec, func, *args, **kw)
        func(*args, **kw)
    t = threading.Timer(sec, wrapper)
    t.start()
    return t

if __name__ == "__main__":
    set_interval(3,hello,"world.")











































