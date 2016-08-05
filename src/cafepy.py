#!/usr/bin/env python3
# coding: utf-8
"""
### Author: Mogu ###
This code is for analyizing CafeMol Outputs.
CafeMol which is one of the Molecular Dynamics simulation software 
is developed by Takada-Lab in Kyoto Univ. .

# environment:
    Python3.5.1
# requirements:

"""

import argparse

### My module
#import calc_distance
import calc_com

class CafePy(object):
    #This class is main class of cafepy and analyizes command-line argments.
    def __init__(self):
        self.args = []

    def main(self):
        self._initArgs()
        self.handleArgs()
        
    def handleArgs(self):
        pass
        
    def _initArgs(self):
        message = "Analyzing CafeMol outputs."
        parser = argparse.ArgumentParser(description=message)
        parser.add_argument('calculation_type',nargs='?',type=str,choices=['distance','cmap','com'],help='choose calculation type.')

        
        parser.add_argument('-f','--inputfile',nargs='?',help='input file name[.dcd,.pdb,ninfo,psf]')
        
        args = parser.parse_args()
        print(args)
        return args
        
if __name__ == "__main__":
    tmp = CafePy()
    tmp.main()
    

