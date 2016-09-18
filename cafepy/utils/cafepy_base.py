# fileencoding: utf-8
"""
:Editer:    Mogu
:Version: 0.0.1dev
:environment:  Pyton3.5.1

*Contents*

* CafePyBase
"""


import os
import sys


from .cafepy_error import FileTypeError
from ..files.dcdfile import DCD
from ..files.pdbfile import PDB
from ..files.indexfile import Index


class CafePyBase(object):
    """
    This class provides CafePy Base Class.

    """
    
    def __init__(self):
        self.filename = ''


    def read(self, filename):
        sfx = getSuffix(filename)
        data = None

        if sfx == 'pdb':
            data = PDB(filename)
        elif sfx == 'dcd':
            data = DCD(filename)
        elif sfx == 'ndx':
            data = Inde(filename)
        else:
            msg = 'Please set a suffix of file in [pdb, dcd, ndx, psf]'
            raise FileTypeError(msg)

        return data
        

    def getSuffix(self, filename):
        return filename.split('.')[-1]


    def _readPDB(self):
        pass

    def _readDCD(self):
        pass

    def _readIndex(self):
        pass

    
    
