#!/bin/env python

def read():
    try:
        fp = open('test.txt','r')
        lines = fp.readlines()
        for line in lines:
            if line.endswith('\n'):
                print line.strip()
            else:
                print line
    except:
        print "something is wrong."
    finally:
        fp.close()

if __name__ == "__main__":
    read()

