#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-3-3
# Version: 1.0

import signal
import sys

def signal_handler(signal, frame):
    print "You pressed Ctrl+C!"
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print "Press Ctrl+C"

    signal.pause()











































