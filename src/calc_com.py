#!/usr/bin/env python3
# coding:utf-8
"""
###  Editer:Mogu  ###
This class caluclates the center of mass of proteins from [dcd,pdb]-files.

environment:
    Pyton >= 3.5.1
requirement:
    Numpy >= 1.11
    Scipy >= 
example:
    cafepy com -i test.pdb[.dcd]
"""


## 3rd Parties
import numpy as np
import scipy as sc

## My module
from read_dcd import ReadDCD
from read_pdb import ReadPDB
from read_index import ReadIndex

class CalcCOM(object):
    """
    Calculating the center of mass from [dcd,pdb]-files
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
        self.dcdfile = ""
        self.pdbfile = ""
        self.data = []
        
    def readDCD(self,inputfile):
        self.dcdfile = inputfile
        self.data = ReadDCD()
        self.data.main(inputfile)

        
    def readPDB(self):
        #
        pass

    
    def readIndex(self):
        pass

    def calcCOMfromPDB(self):
        pass

    def calcCOMfromDCD(self,index=[]):
        """ Calculating the Center of mass from DCD-file."""
        if not index:
            self.com = np.average(self.data[:],axis=0)
            print(self.com)
        else:
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
    
