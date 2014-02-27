#!/bin/env python

import logging
import argparse











parser = argparse.ArgumentParser()
parser.add_argument("-e", "-echo", help="echo the string you use here", action="store_true")
args = parser.parse_args()
if args.echo:
    print "echo turned on."
