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
from .file_io import FileIO
from .read_dcd import DCD
from .read_pdb import PDB
from .read_index import Index
from .write_movie import WriteMovie

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
        # pycafe.py com -f [dcd,pdb]-infile [optional: -o outfile, -nf index.file or -n int-value] 
    """
    def __init__(self):
        self.dcdfile = ""
        self.pdbfile = ""
        self.data = []
        
    def readDCD(self,inputfile):
        self.dcdfile = inputfile
        self.data = DCD()
        self.data.main(inputfile)
        
    def readPDB(self):
        #
        pass

    def readIndex(self):
        pass

    def calcCOMfromPDB(self):
        pass

    def calcCOMfromDCD(self,atom_index=[],traj_index=[]):
        """ 
        ### Calculating the Center of mass from DCD-file.
        atom_index    :  You can select Atom for calculating COM with index[.ndx,.ninfo]-file 
        traj_index  :  You can extract trajectories for calculating COM.
        
        """
        if not atom_index:
            self.com = np.average(self.data[:],axis=0)
        else:
            ndata = np.array(self.data)
            self.com = np.average(ndata[:,atom_index],axis=0)
            del ndata


    def writeFile(self,outputfile,header= ""):
        np.savetxt(outputfile,self.com,header=header,fmt="%.8e")

        
    def writeShow(self):
        pass

    def close(self):
        self.data.close()
    
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
    
