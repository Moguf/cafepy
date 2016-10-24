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

class CafePyBase(object):
    """
    This class provides CafePy Base Class.

    """
    
    def __init__(self):
        self.filename = ''
        self.sfx = ''

    def read(self, filename):
        """
        read [pdb, dcd, index] files. This function define reading type from files suffix. you need to set a proper suffix with filename.

        :inputs:  filename(str)
        :return:  class [DCD, PDB, Index]

        """
        from ..files.dcdfile import DCD
        from ..files.pdbfile import PDB, CGPDB
        from ..files.indexfile import Index
        from ..files.ninfofile import Ninfo        

        self.filename = filename
        sfx = self.getSuffix(filename)
        self.sfx = sfx
        data = None

        if sfx == 'pdb':
            try:
                data = PDB(filename)
            except ValueError:
                data = CGPDB(filename)

        elif sfx == 'dcd':
            data = DCD(filename)
        elif sfx == 'ninfo':
            data = Ninfo(filename)
        elif sfx == 'ndx':
            data = Index(filename)
        else:
            msg = 'Please set a suffix of file in [pdb, dcd, ndx, psf]'
            raise FileTypeError(msg)
        return data
        

    def getSuffix(self, filename):
        return filename.split('.')[-1]


    def _readIndex(self):
        pass


    def setClibPath(self):
        sys.path.append((os.path.join(os.path.dirname(__file__), '../../build/lib.*/')))

    
