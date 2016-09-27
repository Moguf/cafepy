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

from scipy.spatial.distance import euclidean as euc

from ..utils.cafepy_base import CafePyBase

class CalcDistance(CafePyBase):
    """
    Calculating the distance between atoms.

    *Examples*

    .. code-block:: python

        # filename = [pdb, dcd]-file
        tmp = CalcDistance(filename)
        tmp.calcDist()
        tmp.dist_data()

    .. code-block:: bash    
        # pycafe.py com -i [dcd,pdb]-infile [optional: -o outfile, -n index.file or int-value] 
    
    *Members*
    
    :self.index:   Index class.
    :self.filename:  dcd or pdb file path.
    :self.pairlist:  this values is came from self.index.
    :self.dist_data:  contains result after calculating pair distances.

    """
    def __init__(self, filename, index=''):

        self.index = []
        self.filename = filename
        self.data = self.read(filename)
        self.index = self.getIndex(index)
        self.pairlist = self.makePair(self.index)
        self.dist_data = [[] for i in range(len(self.pairlist))]

    def run(self):
        '''
        calculate distances between given pairs.
        :inputs:  None
        :return:  results
        '''
        
        out = []
        if self.data.ftype == 'dcd':
            out = self._calcDistDCD()
        elif self.data.ftype == 'pdb':
            out = self._calcDistPDB()
        return out
    
    def _calcDistDCD(self):
        '''
        calculate distances between given pairs from PDB files.
        this class is called from self.calcDist()

        :args:  
        :return:  Distances (list)
        '''
        for icoord in self.data:
            for i, pair in enumerate(self.pairlist):
                self.dist_data[i].append(euc(icoord[pair[0]],icoord[pair[1]]))
        return self.dist_data
        
    def _calcDistPDB(self):
        '''
        calculate distances between given pairs from PDB files.
        this class is called from self.calcDist()
        :args:  
        :return:  Distances (list)
        '''
        for i, pair in enumerate(self.pairlist):
            self.dist_data[i] = euc(self.data[pair[0]],self.data[pair[1]])
        return self.dist_data

    def makePair(self, index):
        '''
        make pairs from index[list-foarmat]
        :Args:  index
        :return:  pairs (list)
        '''
        pairlist = []
        for i in range(len(index))[::2]:
            pairlist.append([index[i], index[i+1]])
        return pairlist
            
    def getIndex(self, index):
        '''
        get indexes from file for list.
        :Args:  index (filename or list-format)
        :return:  self.index ( list-format )
        '''
        if isinstance(index, str):
            self.index = self.read(index).data
        elif isinstance(index, list):
            self.index = index
        if len(self.index)%2 != 0:
            msg = 'len(index) must be an even number.'
            raise Exception(msg)
        return self.index

    def writeFile(self):
        pass

    def writeShow(self):
        pass

    
