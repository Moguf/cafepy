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
        self.filename = ''

    def openFile(self, filename, mode='r'):
        """

        """
        _file = None
        try:
            _file = open(filename, mode)
        except:
            raise FileExistsError
        return _file
    
    def closeFile(self):
        pass
        
    def __str__(self):
        pass

    
    
