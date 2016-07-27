#!/usr/bin/env python3
# coding: utf-8
"""
This code is for analyizing CafeMol Outputs.
CafeMol which is one of the Molecular Dynamics simulation software 
is developed by Takada-Lab in Kyoto Univ. .
"""

import argparse

class CafePy(object):
    #This class is main class of cafepy and analyizes options.
    def __init__(self):
        pass

    def main(self):
        self.initArgs()

    def initArgs(self):
        message = "Analyzing CafeMol outputs."
        parser = argparse.ArgumentParser(description=message)
        parser.add_argument('calculation_type',nargs='?',type=str,choices=['distance','cmap','com'],help='choose calculation type.')
        parser.add_argument('-i','--infile',nargs='?',help='input file name[.dcd,.pdb,ninfo,psf]')
        
        args = parser.parse_args()

        
if __name__ == "__main__":
    tmp = CafePy()
    tmp.main()
    

