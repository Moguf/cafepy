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

    def run(self, atom_idx=[], unit_idx=[], traj_idx=[]):
        """ 
        Calculates the Center of mass from DCD-file or PDB-file.

        :Args: atom_idx (list), traj_idx (list)

            :atom_idx:    You can select Atoms for calculating COM with idx[.ndx,.ninfo]-file 
            :unit_idx:    You can select Units in pdb format.
            :traj_idx:    You can extract trajectories for calculating COM.

        """
        
        if self.sfx == 'dcd':
            return self._dcdrun(atom_idx, unit_idx, traj_idx)
        elif self.sfx == 'pdb':
            return self._pdbrun(atom_idx, unit_idx)
        
    def _dcdrun(self, atom_idx=[], unit_idx=[], traj_idx=[]):
        if not atom_idx:
            self.com = np.average(self.data[:], axis=1)
        else:
            ndata = np.array(self.data)
            self.com = np.average(ndata[:, atom_idx], axis=1)
        return self.com

    def _pdbrun(self, atom_idx=[], unit_idx=[]):
        if unit_idx:
            _data = []
            for i in unit_idx:
                i = i-1
                if i == 0:
                    s = 0
                else:
                    s = sum(self.data.info['aasize'][:i])
                e = sum(self.data.info['aasize'][:i+1])
                _data += self.data[:][s: e]
            ndata = np.array(_data)
            self.com = np.average(ndata, axis=0)
        elif not atom_idx:
            self.com = np.average(self.data[:], axis=0)
        return self.com

    def writeFile(self, outputfile, header= ""):
        np.savetxt(outputfile, self.com, header=header, fmt="%.8e")

    def writeShow(self):
        pass

    def close(self):
        self.data.close()
        
