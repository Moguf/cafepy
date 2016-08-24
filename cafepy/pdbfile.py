#!/usr/bin/env python3
# coding:utf-8
"""
###  Editer:Mogu  ###
class:
    PDB: reading PDB(Protein data Bank)-files.
environment:
    Pyton3.5.1
requirement:
    ?Numpy1.10.1
caution:
    python3: supporting that str is utf-8 type.
    We need to write [b"sgring"].
"""
import os
import re
import sys

#### Third Parties
#import numpy as np

#### My Module
from .file_io import FileIO
from .cafepy_error import ReadingError,FileError
from .cafepy_base import CafePyBase
        
class PDB(CafePyBase,FileIO):
    """
    Reading a PDB(Protein Data Bank) file which is an output from CafeMol Software.
    """
    def __init__(self, iofile):
        FileIO.__init__(self)
        self.iofile = iofile
        self.coard = []
        self.row_data = []
        
    def readATOM(self):
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
                self.row_data.append([slc[2](line[slice(*slc[:2])]) for slc in _format])
        return self.row_data

    def __getitem__(self,key):
        if isinstance(key,slice):
            return [self[i] for i in range(*key.indices(len(self)))]
        elif isinstance(key,int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError("The index (%d) is out of range." % key)
            return self.row_data[key][5:8]
        else:
            raise TypeError("Invalid argument type.")

    def __len__(self):
        return len(self.row_data)

    def read(self):
        self._file = self.openFile(self.iofile)
        return self.readATOM()

    def close(self):
        self._file.close()
        return True
        
    def write(self, xyz=[], inpsffile=""):
        
        
        pass
    
class CGPDB(CafePyBase, FileIO):
    """
    Reading a Coarse-Grained PDB(Protein Data Bank) file which is an output from CafeMol Software.
    """
    def __init__(self):
        pass

    
if __name__ == "__main__":
    tmp = PDB()
    tmp.main()
    

