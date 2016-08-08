#!/usr/bin/env python3
# coding:utf-8
"""
###  Editer:Mogu  ###
This class supports fundamental class for reading and writing files.

environment:
    Pyton3.5.1
requirement:

"""


class FileIO(object):
    """
    This class fundamental class for reading and writing files.
    Don't support command line usages.
    """
    def __init__(self):
        self.inputfile = ""
        self._file = ""

    def openFile(self,filename,mode='r'):
        try:
            self._file = open(filename,mode)
        except:
            raise TypeError
        
        return self._file

    def closeFile(self):
        pass
        
    def __str__(self):
        pass

    
    
