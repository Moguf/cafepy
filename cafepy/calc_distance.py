#!/usr/bin/env python3
# coding:utf-8
"""
###  Editer:Mogu  ###
This class caluclates the distance between atoms from [dcd,pdb]-files.

environment:
    Pyton3.5.1
requirement:

example:
    cafepy distance -f test.dcd[.pdb]
"""

from .read_dcd import ReadDCD
from .read_pdb import ReadPDB
from .read_index import ReadIndex

class CalcDistance(object):
    """
    Calculating the distance between atoms
    Examples:
    # In Python scripts.
        tmp = CalcCom()
        tmp.readDCD("dcdfile")   or  tmp.readPDB("pdbfile")
        tmp.calcCOMfromDCD()     or  tmp.calcCOMfromPDB()
        tmp.writeFile("outfile") or  tmp.writeShow()
    # In Terminal.
        # pycafe.py com -i [dcd,pdb]-infile [optional: -o outfile, -n index.file or int-value] 
    """
    def __init__(self):
        pass

    def readDCD(self):
        #
        pass

    def readPDB(self):
        #
        pass

    def readIndex(self):
        pass

    def calcCOMfromPDB(self):
        pass

    def calcCOMfromDCD(self):
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
    
