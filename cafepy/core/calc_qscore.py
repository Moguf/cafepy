#!/usr/bin/env python3
# fileencoding:utf-8
"""
Calculating Q-score from DCD-format or PDB-format files.

This module contains CalcQscore class. The class provides methods for 
calculating Q-score. Q-Score is a value for indicating how a protein 
structure is similar to native strucutre. The value ranges from 0 (denature)
to 1.0(nature).

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
    Calculating Q-Score.

    The class provides methods for calculating Q-score. Q-Score is a value for 
    indicating how a protein structure is similar to native strucutre. The value
    ranges from 0 (denature) to 1.0(nature).
    
    .. code-block:: 

        # filename = [pdb, dcd]-file
        tmp = CalcQscore(filename)
        tmp.run():
        tmp.writeFile("outfile") or  tmp.writeShow()

    .. code-block:: bash

        # In Terminal.
        pycafe.py com -i [dcd,pdb]-infile [optional: -o outfile, -n index.file or int-value] 
    """
    
    def __init__(self, filename, ninfo='', cutoff=12.0):
        self.filename = filename
        self.data = self.read(filename)
        self.ninfo = self.read(ninfo)
        
    def run(self):
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

    
