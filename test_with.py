#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-3-4
# Version: 1.0

class Test():
    def __enter__(self):
        print "in enter."
    def __exit__(self, t, v, b):
        print "in exit."

if __name__ == "__main__":
    with Test() as test:
        print "in with."











































