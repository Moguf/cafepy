#!/usr/bin/env python3
# coding:utf-8
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

from ..files.dcdfile import DCD
from ..files.pdbfile import PDB
from ..files.indexfile import Index

class CalcDistance(object):
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
    def __init__(self, filename):
        self.dcd = None
        self.pdb = None
        self.index = None
        self.filename = filename
        self._read(filename)

    def _read(self, filename=""):
        suffix = filename.split('.')[-1]
        
        
        
        
    def readDCD(self):
        self.dcd = DCD(filename)

    def readPDB(self):
        self.pdb = PDB(filename)

    def readIndex(self):
        self.index = Index(filename)
        

    def calcDist(self):
        pass
    

    def writeFile(self):
        pass

    def writeShow(self):
        pass

    
    def main(self):
        """
        Supporting comand line interfaces.
        # Examples:
            calc_com.py -i [dcd,pdb]-file [optional: -o outfile, -n index.file or int-values] 
        """
        pass

    
if __name__ == "__main__":
    tmp = CalcCOM()
    tmp.main()
    
