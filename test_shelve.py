#!/bin/env python
#-*- coding=utf-8 -*-
# Author:  John Hu
# Email:   huzichunjohn@126.com
# Date:    2014-3-5
# Version: 1.0

import shelve

def save_data():
    try:
        db = shelve.open('db.dat', 'c')
        db['int'] = 1
        db['float'] = 2.3
        db['string'] = "hello world."
        db['key'] = 'value'
    finally:
        db.close()

def read_data():
    db = shelve.open('db.dat', 'r')
    for item in db.items():
        print item
    db.close()

if __name__ == "__main__":
    save_data()
    read_data()
















































