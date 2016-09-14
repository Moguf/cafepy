#!/usr/bin/env python3
"""
Usage:
    copy outputs to cafepy.rst.

"""


import re, os, sys, glob
from importlib import import_module

sys.path.append('../cafepy/')

header_template = """
{}
============================

.. automodule:: {}

"""

auto_class_template = """

.. autoclass:: {}
    :members: {}


"""

class CafePyDocs():
    def __init__(self):
        self.py_files = glob.glob('../cafepy/**/[a-zA-Z]*.py')
        self.doc_path = 'source/codes/'
        
    def makeFiles(self):
        for filepath in self.py_files:
            ilist = filepath.split('/')
            name = filepath.split('/')[-1][:-3]
            module = '.'.join(filepath.split('/')[1:-1])
            classes = self.getClasses(filepath)
            htmp =  header_template.format(name, module + '.' + name)
            mod = import_module(module + '.' + name)
            clstmp = ''
            for icls in classes:
                cls = getattr(mod, icls)
                med = self.getMethods(dir(cls))
                medstr = ', '.join(med)
                clstmp += auto_class_template.format(icls, medstr)

            txt = htmp + clstmp
            dicy = ilist[-2]
            fname = self.py2rst(ilist[-1])
            print("    " + self.doc_path[7:] + dicy + '/' + fname[:-4])
            with open(self.doc_path + dicy + '/' + fname, 'w') as f:
                f.write(txt)

    def getMethods(self, dirs):
        out = []
        for idir in dirs:
            if idir[0] != '_':
                out.append(idir)
        return out
            
    def py2rst(self, file_py):
        return file_py[:-3] + ".rst"

    def getDirs(self):
        dirs = [ idir.split('/')[-2] for idir in self.py_files]
        return list(set(dirs))

    def makeDirs(self):
        dirs = self.getDirs()
        path = 'source/codes/'
        for idir in dirs:
            ipath = path + idir
            try:
                os.mkdir(ipath)
            except FileExistsError:
                print("Exists:\t\tdocs/" + ipath)

    def getClasses(self, filename):
        classes = []
        with open(filename, 'r') as f:
            for iline in f.readlines():
                m = re.match('^class (\w+)\(.*\)', iline)
                if m:
                    classes.append(m.group(1))
        return classes
                    
    def main(self):
        self.makeDirs()
        self.makeFiles()

if __name__ == '__main__':
    tmp = CafePyDocs()
    tmp.main()
