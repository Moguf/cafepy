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
import os
import sys
from ..utils.cafepy_base import CafePyBase


class CalcQscore(CafePyBase):
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
    def __init__(self, filename, ninfo='', cutoff=12.0):
        
        import qscore
        self.filename = filename
        self.data = self.read(filename)
        self.ninfo = self.read(ninfo)
        
    def calcDist(self):
        if self.data.ftype == 'dcd':
            print(">>>>", self.data[:])
            

    def readNinfo(self):
        pass
            

    def writeFile(self):
        pass

    def show(self):
        pass

    def save(self, outfile):
        pass

    
