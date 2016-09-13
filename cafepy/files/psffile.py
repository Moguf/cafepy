#!/usr/bin/env python3
# coding:utf-8
import os
import sys

from file_io import FileIO

class PSF(FileIO):
    def __init__(self, iofile):
        self.iofile = iofile

    def read(self):
        self.openFile()
        self._read()

    def _read(self):
        pass

    def close(self):
        pass

    def write(self):
        pass

if __name__ == '__main__':
    pass
        
