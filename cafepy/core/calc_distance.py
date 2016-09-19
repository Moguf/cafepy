#!/usr/bin/env python3
# fileencoding:utf-8
"""
:Editer:    Mogu
:Version: 0.0.1dev
:environment:  Pyton3.5.1

*contants*

* CalcDistance: provide calculating the distance.

This class caluclates the distance between atoms from [dcd, pdb]-files.

example:
    cafepy distance -f test.dcd[.pdb]
"""

from ..utils.cafepy_base import CafePyBase

class CalcDistance(CafePyBase):
    """
    Calculating the distance between atoms
    Examples:
    # In Python scripts.
        # filename = [pdb, dcd]-file
        tmp = CalcDistance(filename)
        tmp.calcDist():
        tmp.writeFile("outfile") or  tmp.writeShow()
    # In Terminal.
        # pycafe.py com -i [dcd,pdb]-infile [optional: -o outfile, -n index.file or int-value] 
    """
    def __init__(self, filename, index=''):
        self.dcd = None
        self.pdb = None
        self.index = None
        self.filename = filename
        self.data = self.read(filename)
        self.index = self.getIndex(index)
        
    def calcDist(self):
        if self.data.ftype == 'dcd':
            print(">>>>", self.data[:])
        
    def getIndex(self, index):
        if index:
            if isinstance(index, str):
                self.index = self.read(index)
            elif isinstance(index, list):
                self.index = index
        return self.index

    def writeFile(self):
        pass

    def writeShow(self):
        pass

    
