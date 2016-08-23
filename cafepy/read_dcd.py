#!/usr/bin/env python3
# coding:utf-8
"""
###  Editer:Mogu  ###
class:
    DcdHeadr: defines dcd-headers structure.
    ReadDcd: reads dcd-files.
environment:
    Pyton3.5.1
requirement:
    ?Numpy1.10.1
referance:
    Author:Naoto Hori,  https://github.com/naotohori/
    Author:mash-ito,    https://github.com/mash-it/
caution:
    python3: supporting that str is utf-8 type.
    We need to write [b"sgring"].
"""
import os
import sys
import struct

#### Third Parties
#import numpy as np

#### My Module
from .file_io import FileIO
from .cafepy_error import ReadingError,FileError
from .cafepy_base import CafePyBase

class DcdHeader:
    """
    """
    def __init__(self):
        self.nset = None
        self.istart = None
        self.nstep_save = None
        self.nstep = None
        self.nunit_real = None
        self.delta = None
        self.title = None
        self.tempk = None
        self.lunit2mp = None
        self.nmp_real = None
        self.bsize = 0
        self.tstep = None
        
    def show(self):
        for line in self.title :
            print(line)
        print(b'nset', self.nset)
        print(b'istart', self.istart)
        print(b'nstep_save', self.nstep_save)
        print(b'nstep', self.nstep)
        print(b'nunit_real', self.nunit_real)
        print(b'delta', self.delta)
        print(b'tempk', self.tempk)
        for i in range(self.nunit_real) :
            print(b'lunit2mp[', i, ']', self.lunit2mp[i])
        print(b'nmp_real', self.nmp_real)

        
class DCD(CafePyBase,FileIO):
    """
    Reading a DCD file which is an output from CafeMol Software.
    """
    def __init__(self):
        self.inputfile = ""
        self._file = ""
        self._header = DcdHeader()
        self.length = None
        
    def readHeaderSize(self):
        self._file.seek(0)
        for i in range(3):
            tmp = struct.unpack('i',self._file.read(4))[0]
            self._file.seek(tmp,os.SEEK_CUR)
            self._file.seek(4,os.SEEK_CUR)
        self._header.bsize = self._file.tell()
        
    def readHeader(self):
        self._file.seek(0)
        # first block 
        b = self._pick_data()
        bdata = struct.unpack('4siii5iifi9i', b)

        #bdata = struct.unpack('4siii5iid9i',b)
        if bdata[0] != b'CORD' :
            msg = "CAUTION:%s is not Dcd formats." % self.inputfile
            raise FileError(__file__,"readHeader()",msg)

        self._header.nset = bdata[1]
        self._header.istart = bdata[2]
        self._header.nstep_save = bdata[3]
        self._header.nstep = bdata[4]
        self._header.nunit_real = bdata[5]
        self._header.delta = bdata[10]
        self._header.tstep = bdata[4] / bdata[3]

        # title block (number of line can be changed)
        b = self._pick_data()
        bdata = struct.unpack(('i' + '80s' * (3 + self._header.nunit_real)), b)
        
        self._header.title = (bdata[1], bdata[2])
        #self._header.tempk = float(bdata[3].strip('\0 '))
        self._header.tempk = float(bdata[3])
        self._header.lunit2mp = []
        for i in range(self._header.nunit_real) :
            #self._header.lunit2mp.append(int(bdata[i + 4].strip('\0 ')))
            self._header.lunit2mp.append(int(bdata[i + 4]))
            
        # nmp_real
        b = self._pick_data()
        self._header.nmp_real = struct.unpack('i', b)[0]

    def _pick_data(self):
        """return binary data between 'integer' and 'integer'. 'integer' indicates the number of bytes"""
        num = struct.unpack('i', self._file.read(4))[0]
        b = self._file.read(num)
        self._file.seek(4, os.SEEK_CUR)
        return b
    
    def _readOneFrame(self):
        coord_matrix = []
        b = self._pick_data()
        x = struct.unpack('f' * self._header.nmp_real, b)
        b = self._pick_data()
        y = struct.unpack('f' * self._header.nmp_real, b)
        b = self._pick_data()
        z = struct.unpack('f' * self._header.nmp_real, b)
        
        for i in range(self._header.nmp_real) :
            xyz = [x[i], y[i], z[i]]
            coord_matrix.append(xyz)
        return coord_matrix

    
    def __getitem__(self,key):
        """
        Supporting to get item with an index and slice. ex. self[1],self[2:4]
        @Referance:
        http://stackoverflow.com/questions/2936863/python-implementing-slicing-in-getitem
        """
        if isinstance(key,slice):
            return [self[i] for i in range(*key.indices(len(self)))]
        elif isinstance(key,int):
            if key < 0:
                key += len(self)
            if key <0 or key >= len(self):
                raise IndexError("The index (%d) is out of range." % key)
            self.readHeaderSize()
            self._file.seek(0)
            self._file.seek(self._header.bsize)
            stepsize = 3 * 4 * (self._header.nmp_real + 2)
            self._file.seek(stepsize * key,os.SEEK_CUR)
            return self._readOneFrame()
        else:
            raise TypeError("Invalid argument type.")
        
        """
        File contents.        
        bytesize(long integer) x cordinate(double) * The Number of atoms bytesize(long integer)
        bytesize(long integer) y cordinate(double) * The Number of atoms bytesize(long integer)
        bytesize(long integer) z cordinate(double) * The Number of atoms bytesize(long integer)
        
        Example:(test.dcd)
        228(long int) 57 * 4(x cordinate double) 228(long int) 
        228(long int) 57 * 4(y cordinate double) 228(long int)
        228(long int) 57 * 4(z cordinate double) 228(long int)
        ===> stepszie = 4+57*4+4 = 4*(57+2)
        """

    def __len__(self):
        """  Returning total step of trajectory. """
        if self.length:
            return self.length
        
        if self._header.tstep == None:
            raise ReadingError(__file__,"__len__","Header information is Nothing!!")
        
        self._file.seek(self._header.bsize)
        stepsize = 3 * 4 * (self._header.nmp_real + 2) - 4
        """
        stepsize = 
        (int(4)) x cords(4) int(4)
        int(4)   y cords(4) int(4)
        int(4)   z cords(4) int(4)
        = int(4)*5 + xyz cords(4)
        """
        step = 0
        try:
            while(True):
                integer = struct.unpack('i',self._file.read(4))[0]
                self._file.seek(stepsize,os.SEEK_CUR)
                step += 1
        except:
            step -= 1
            if step != self._header.tstep + 1:
                msg = "CAUTION::Total steps(%9d) in Header != Total steps(%9d) in Dcd" % (self._header.tstep + 1,step)
                print(msg)
            self.length = step
            return step

    def close(self):
        self._file.close()
        
    def main(self,inputfile):
        self.openFile(inputfile,mode="rb")
        self.readHeader()
        
if __name__ == "__main__":
    pass

    
    
