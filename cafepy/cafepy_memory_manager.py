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
    1) in Ch13.4 Python Coookbook,Third edition [By David Beazley,Brian K. Jones], 2013.

"""

import resource

class CafeMemManager:
    def __init__(self):
        self.maxsize = 16

    def setLimitMemory(self,maxsize):
        # set Max Memory size.
        # maxsize:unit is Gb.
        self.maxsize = 1024*1024*1024*maxsize
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        resource.setrlimit(resource.RLIMIT_AS,(self.maxsize,hard))
        print('Set Memoy Limit\t:\t{}Gb;'.format(maxsize))
        
if __name__ == '__main__':
    pass
    
