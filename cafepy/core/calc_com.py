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
from ..utils.cafepy_base import CafePyBase

class CalcCOM(CafePyBase):
    """
    Calculating the center of mass from [dcd,pdb]-files

    * Examples:
    
    .. code-block:: python

        tmp = CalcCom("filename") # both dcd-format and pdb-format are ok
        tmp.run()
        tmp.writeFile("outfile") or  tmp.writeShow()

    *In Terminal.*

    .. code-block:: bash

         pycafe.py com -f [dcd,pdb]-infile [optional: -o outfile, -nf index.file or -n int-value] 
    """
    def __init__(self, inputfile, *args, **kargs):
        self.dcdfile = ""
        self.pdbfile = ""
        self.data = []
        self.com = []
        self._read(inputfile)
        
    def _read(self, inputfile):
        self.data = self.read(inputfile)   # from CafePyBase
        
    def readIndex(self):
        pass

    def run(self, atom_indexes=[], unit_indexes=[], traj_indexes=[]):
        """ 
        Calculates the Center of mass from DCD-file or PDB-file.

        :Args: atom_indexes (list), traj_indexes (list)
            :atom_indexes:    You can select Atom for calculating COM with indexes[.ndx,.ninfo]-file 
            :traj_indexes:    You can extract trajectories for calculating COM.

        """
        if self.sfx == 'dcd':
            return self._dcdrun(atom_indexes, unit_indexes, traj_indexes)
        elif self.sfx == 'pdb':
            return self._pdbrun(atom_indexes, unit_indexes)
        
    def _dcdrun(self, atom_indexes=[], unit_indexes=[], traj_indexes=[]):
        if not atom_indexes:
            self.com = np.average(self.data[:], axis=1)
        else:
            ndata = np.array(self.data)
            self.com = np.average(ndata[:, atom_indexes], axis=1)
        return self.com

    def _pdbrun(self, atom_indexes=[], unit_index=[]):
        if not atom_indexes:
            self.com = np.average(self.data[:], axis=0)
        else:
            ndata = np.array(self.data)
            self.com = np.average(ndata[:, atom_indexes], axis=1)
        return self.com
        
            

    def writeFile(self, outputfile, header= ""):
        np.savetxt(outputfile, self.com, header=header, fmt="%.8e")

    def writeShow(self):
        pass

    def close(self):
        self.data.close()
        
