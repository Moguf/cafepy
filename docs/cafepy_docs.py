#!/usr/bin/env python3

import os, sys, glob

cafepy_files = glob.glob('../cafepy/files/[a-zA-Z]*.py')
cafepy_utils = glob.glob('../cafepy/utils/[a-zA-Z]*.py')
cafepy_core = glob.glob('../cafepy/core/[a-zA-Z]*.py')

dirs = ['files', 'utils', 'core']

print(cafepy_files)
print(cafepy_utils)
print(cafepy_core)

def make_files():
    pass

def make_dirs():
    path = 'source/codes/'
    for idir in dirs:
        ipath = path + idir
        try:
            os.mkdir(ipath)
        except FileExistsError:
            print("Exists:" + ipath)
        

make_dirs()    
