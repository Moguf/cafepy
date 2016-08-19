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
from cafepy_error import CmdLineError,FileError
from calc_com import CalcCOM
from cafepy_memory_manager import cafeMemManager

class CafePy(object):
    #This class is main class of cafepy and analyizes command-line argments.
    def __init__(self):
        cMM = cafeMemManager()
        cMM.setLimitMemory(16)
        ## Memory Limit: 16 Gb.
        self.args = []
        self.calc_msg = {}
        self.header = ""
        self.initSet()
        
    def main(self):
        self._initArgs()
        self.handleArgs()

    def initSet(self):
        self.calc_msg["com"] = "Center of Mass."

        
    def handleArgs(self):
        ctype = self.args.calculation_type
        header = "CALCULATION\t\t:\t{};".format(self.calc_msg[ctype])
        self.header += header
        print(header)
        
        if None == ctype:
            msg = "\nCAUTION:calculation_type is not set!!\n"
            msg += "CAUTION:choise ['distance','cmap','com']\n"
            msg += "PLEASE: cafepy -h "
            raise CmdLineError(msg)
        
        if "com" == ctype:
            self.checkFlags(self.args,'i','o')
            com = CalcCOM()
            com.readDCD(self.args.inputfile)
            com.calcCOMfromDCD()
            com.writeFile(self.args.outputfile,self.header)
            com.close()
            return
        
    def checkFlags(self,args,*flags):
        if 'i' in flags:
            msg = "\nCOUTION: No ouput_file !! ex) cafepy [...] -f input-file"
            self._checkArg(args.inputfile,msg)
            header = "INPUTFILE\t\t:\t{};".format(args.inputfile)
            print(header)
            self.header += header

        if 'o' in flags:
            msg = "\nCOUTION: No input_file !! ex) cafepy [...] -o output-file"
            self._checkArg(args.outputfile,msg)
            header = "OUTPUTFILE\t\t:\t{};".format(args.outputfile)
            print(header)
            self.header += header
    

    def _checkArg(self,arg,msg):
        if not arg:
            msg = msg
            raise FileError(msg)
        
    def _initArgs(self):
        message = "Analyzing CafeMol outputs."
        parser = argparse.ArgumentParser(description=message)
        parser.add_argument('calculation_type',nargs='?',type=str,choices=['distance','cmap','com'],help='choose calculation type.')

        
        parser.add_argument('-f','--inputfile',nargs='?',help='input file name[.dcd,.pdb,ninfo,psf]')
        parser.add_argument('-o','--outputfile',nargs='?',help='output file name[.dat]')
        
        self.args = parser.parse_args()

        return self.args
        
if __name__ == "__main__":
    tmp = CafePy()
    tmp.main()
    

