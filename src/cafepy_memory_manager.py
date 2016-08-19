#!/usr/bin/env python3
# coding:utf-8
"""
### Author: Mogu ###
This file contains Memory manager Class. 
Python don't set Memory Limit.We need to set Memory Limit to protect our Machine from a pending state.
# Environment:
    Python3.5.1
# Requirements:

# References:
    1) in Ch13.4 Python Coookbook,Third edition [By David Beazley,Brian K. Jones]

"""

import resource

class cafeMemManager:
    def __init__(self):
        pass
    def setLimitMemory(self,maxsize):
        # set Max Memory size.
        # maxsize:unit is Gb.
        maxsize *= 1024*1024*1024
        print(getattr(resource.getrusage(resource.RUSAGE_SELF),'ru_ixrss'))
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        resource.setrlimit(resource.RLIMIT_AS,(maxsize,hard))


if __name__ == '__main__':
    tmp = cafeMemManager()
    
