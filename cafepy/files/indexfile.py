#!/usr/bin/env python3
# coding:utf-8
"""
###  Editer:Mogu  ###
This class read index-file

environment:
    Pyton3.5.1
requirement:

"""
import csv

from .file_io import FileIO

class Index(FileIO):
    """
    Read Index files to choise the number of Atom.

    File format
    -----------
    
        1 2 3 4 5 6 7 8 9 10 11
    
    Methods
    -------
        
    .. methods:: openFile(filename)
        
    

    :_file: file-object
    :data: create list data from read.
    """
    def __init__(self, filename):
        self.data = []
        self.ftype = 'ninfo'
        self.filename = filename
        self.data = self._read(filename)
    
    def _read(self, filename):
        """
        return list-object
        """
        fp = self.openFile(filename,'r')

        out = list(set([int(i) for i in fp.read().split() if i[0] != "#"]))
        ## read integer from file, ignore "#" line ,and dicard dupilicate number.
        
        self.closeFile()
        return out

    
    
