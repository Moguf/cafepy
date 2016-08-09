#!/usr/bin/env python3
# coding:utf-8
"""
###  Editer:Mogu  ###
class:
    WriteMovie: 
environment:
    Pyton3.5.1
requirement:
    ?Numpy1.10.1
caution:
    python3: supporting that str is utf-8 type.
    We need to write [b"sgring"].
"""
import os
import sys


#### Third Parties
#import numpy as np

#### My Module
from file_io import FileIO
from cafepy_error import ReadingError,FileError
from cafepy_base import CafePyBase
        
class WriteMovie(CafePyBase,FileIO):
    """
    Reading a PDB(Protein Data Bank) file which is an output from CafeMol Software.
    """
    def __init__(self):
        pass

    
    def main(self):
        pass

if __name__ == "__main__":
    tmp = WriteMovie()
    tmp.main()
    
    
