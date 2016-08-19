#!/usr/bin/env python3
# coding:utf-8
"""
### Author: Mogu ###
This file contains a class which show an animation in stdout during Caluclaing.

# Environment:
    Python3.5.1
# Requirements:

# References:


"""
import sys
import time
import itertools


class CafepyStdout:
    def __init__(self):
        self.durationtime = 0

    def start(self):
        # set Max Memory size.
        for c in itertools.cycle('|/-\\'):
            sys.stdout.write(c)
            sys.stdout.flush()
            sys.stdout.write('\x08')
            time.sleep(.1)
        
    def end(self):
        pass
    
if __name__ == '__main__':
    import time    
    tmp = CafepyStdout()
    tmp.start()
    tmp.end()
