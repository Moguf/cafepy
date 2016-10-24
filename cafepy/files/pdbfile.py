#!/usr/bin/env python3
# coding:utf-8
"""
:Editer:   Mogu
:Version:   0.0.1dev
:environment:       Pyton3.5.1

PDB: reading PDB(Protein data Bank)-files.


"""

import os
import re
import sys

#### Third Parties
#import numpy as np

#### My Module
from .file_io import FileIO
from ..utils.cafepy_error import CafePyError
from ..utils.cafepy_base import CafePyBase
from ..utils.cafepy_math import rotation3D

class BasePDB(CafePyBase, FileIO):
    def __init__(self, filename):
        FileIO.__init__(self)
        self.ftype = 'pdb'
        self.coard = []
        self.data = []
        self.filename = filename


    def __getitem__(self,key):
        if isinstance(key, slice):
            return [self[i] for i in range(*key.indices(len(self)))]
        elif isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError("The index (%d) is out of range." % key)
            return self.data[key][5:8]
        else:
            raise TypeError("Invalid argument type.")

    def __len__(self):
        return len(self.data)

    def _read(self):
        self._file = self.openFile(self.filename)
        self.readATOM()

    def close(self):
        self._file.close()
        return True
        
    def write(self, xyz=[], inpsffile=""):
        pass

class PDB(BasePDB):
    """
    Reading a PDB(Protein Data Bank) file which is an output from CafeMol Software.
    This class returns coordinates as list format. Please check examples below.
    
    .. note:: This class only read ATOM line.
    
    .. code-block:: python

        from cafepy.files import PDB
    
        pdb = PDB('test.pdb')
        print(pdb[0])
        # you can get the 1th atom xyz coordinate.

        pdb.close()
    
    """
    def __init__(self, filename, *args, **kwargs):
        super(PDB, self).__init__(filename, *args, **kwargs)
        self._read()

    def get(self):
        """
        :input:   None
        :return:  pdb data as list format
        """
        pass
        
    def readATOM(self):
        """
        read ATOM line.
        In future, I will support all record.
        
        :pdb_record:   contains pdb records as list structure.
        :_format:    provides atom line format.
        """
        
        pdb_record = ["HEADER","OBSLTE","TITLE","SPLIT","CAVEAT","COMPND","SOURCE","KEYWDS"\
                    ,"REVDAT","SPRSDE","JRNL","REMARK","DBREF","SEQADV","SEQRES","MODRES"\
                    ,"HET","HETNAM","HETSYM","FORMUL","HELIX","SHEET","SSBOND","LINK","CISPEP"\
                    ,"SITE","CRYST1","ORIGX1","ORIGX2","ORIGX3","SCALE1","SCALE2","SCALE3","MTRIX1"\
                    ,"MTRIX2","MTRIX3","ATOM","ANISOU","TER","HETATM","CONECT","MASTER"]
        _format = [(6,11,int),(12,16,str),(17,20,str),                  #serial,atomName,resName
                   (21,22,str),(22,26,int),                             #chainID,resSeq
                   (30,38,float),(38,46,float),(46,54,float),           #x,y,z
                   (54,60,float),(60,66,float),(76,78,str),(78,80,str)] #occupancy,tempFactor,element,charge
        
        for line in self._file.readlines():
            if re.match(r"(ATOM)", line):
                self.data.append([slc[2](line[slice(*slc[:2])]) for slc in _format])
        return self.data


    
class CGPDB(BasePDB):
    """
    Reading a Coarse-Grained PDB(Protein Data Bank) file which is an output from CafeMol Software.
    """
    def __init__(self, filename, *args, **kwargs):
        super(CGPDB, self).__init__(filename, *args, **kwargs)        
        self.filename = filename
        self.data = []
        self.coords = []
        self.info = {}
        self._read()
        
    def _read(self):
        self._file = self.openFile(self.filename)
        self._readATOM()
        
    def _readATOM(self):
        _format = [(6,11,int),(12,16,str),(17,20,str),                  #serial,atomName,resName
                   (21,22,str),(22,26,int),                             #chainID,resSeq
                   (30,38,float),(38,46,float),(46,54,float)]
        usize = 0
        aasize = []
        each_aasize = 0
        for line in self._file.readlines():
            if re.match(r"(ATOM)", line):
                self.data.append([slc[2](line[slice(*slc[:2])]) for slc in _format])
                each_aasize += 1
            if re.match(r'TER', line):
                aasize.append(each_aasize)
                usize += 1
                each_aasize = 0
        ## the number of amino acid                
        self.info['aasize'] = aasize

        ## the number of amino unit
        if usize == 0:
            self.info['usize'] = 1
        else:
            self.info['usize'] = usize
        return self.data

    def getUnitSize(self):
        pass
        

    def rotation(self, alpha, beta, gamma):
        self.coords = rotation3D(self.coords, alpha, beta, gamma)

    
if __name__ == "__main__":
    tmp = PDB()
    tmp.main()
    

