#!/usr/bin/env python3
# coding:utf-8
"""
This class caluclates the center of mass of proteins from [dcd,pdb]-files.

:Editer:   Mogu
:environment:   Pyton >= 3.5.1
:requirement:   Numpy >= 1.11

* example
.. code-block: bash

    cafepy com -i test.pdb[.dcd]
"""

## 3rd Parties
import numpy as np
import scipy as sc

## My module
from ..files.file_io import FileIO
from ..files.dcdfile import DCD
from ..files.pdbfile import PDB
from ..files.indexfile import Index
from ..files.moviefile import WriteMovie

class CalcCOM(object):
    """
    Calculating the center of mass from [dcd,pdb]-files

    * Examples:
    
    .. code-block:: python

        tmp = CalcCom()
        tmp.readDCD("dcdfile")   or  tmp.readPDB("pdbfile")
        tmp.calcCOM()
        tmp.writeFile("outfile") or  tmp.writeShow()

    *In Terminal.*

    .. code-block:: bash

         pycafe.py com -f [dcd,pdb]-infile [optional: -o outfile, -nf index.file or -n int-value] 
    """
    def __init__(self):
        self.dcdfile = ""
        self.pdbfile = ""
        self.data = []
        self.com = []
        
    def readDCD(self, inputfile):
        self.dcdfile = inputfile
        self.data = DCD(inputfile)
        
    def readPDB(self):
        #
        pass

    def readIndex(self):
        pass


    def calcCOM(self, atom_index=[], traj_index=[]):
        """ 
        Calculates the Center of mass from DCD-file or PDB-file.

        :atom_index:    You can select Atom for calculating COM with index[.ndx,.ninfo]-file 
        :traj_index:    You can extract trajectories for calculating COM.

        """
        if not atom_index:
            self.com = np.average(self.data[:], axis=1)
        else:
            ndata = np.array(self.data)
            self.com = np.average(ndata[:, atom_index], axis=1)

    def writeFile(self, outputfile, header= ""):
        np.savetxt(outputfile, self.com, header=header, fmt="%.8e")

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
    
