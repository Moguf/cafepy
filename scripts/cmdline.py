#!/usr/bin/env python3
# coding: utf-8
"""
:Author:      *Mogu*
:Version:    *0.0.1dev*
:environment:     *Python3.5.1*

This code is for analyizing CafeMol Outputs.
CafeMol which is one of the Molecular Dynamics simulation software 
is developed by Takada-Lab in Kyoto Univ. .

"""
import time
import argparse

### My module

from cafepy.files.dcdfile import DCD
from cafepy.files.indexfile import Index
from cafepy.utils.cafepy_stdout import CafepyStdout
from cafepy.utils.cafepy_error import CmdLineError,FileError
from cafepy.utils.cafepy_memory_manager import CafeMemManager
from cafepy.core.calc_com import CalcCOM


class CafePy(object):
    """ 
    This class is main class of cafepy and analyizes command-line argments. 

    .. note:: Only supports for command line. Don't use this from scripts.

    
    ex) command line usage.

    .. code-block:: bash

        cafepy com -dcd dcdfile -psf psffile 

    
    **Members**

    :anim:     support command line Animation.
    :args:     command line arguments
    :ctype:    calculation type from command line.
    :header:   for command-line message.

    
    **Methods**


    """
    #: Author Mogu
    def __init__(self):
        CMM = CafeMemManager()
        CMM.setLimitMemory(16)
        self.anim = CafepyStdout()
        ## Memory Limit: 16 Gb.
        self.args = []
        self.calc_msg = {}
        self.header = ""
        self._initSet()
        
    def main(self):
        """
        this is main function of CafePy.
        """
        self._initArgs()
        self.handleArgs()

    def _initSet(self):
        self.calc_msg["com"] = "Center of Mass."
        
    def handleArgs(self):
        """
        This method 
        """
        
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
            flags = self._checkFlags(self.args,'f','o','n','nf')
            self.anim.start()
            com = CalcCOM()
            com.readDCD(self.args.inputfile)
            com.calcCOMfromDCD(index=flags['index'])
            com.writeFile(self.args.outputfile,self.header)
            com.close()
            self.anim.end()
            return

        if "readframe" == ctype:
            flags = self._checkFlags(self.args,'f','o','n')
            self.anim.start()
            dcd = ReadDCD()
            dcd.read(self.args.inputfile)
            dcd.write(self.args.outputfile,wtype)
            self.anim.end()
            return

            
        
    def _checkFlags(self, args, *flags):
        """
        test
        """
        out = {}
        if 'f' in flags:
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
            
        if args.indexfile:        
            if 'nf' in flags:
                tmp = Index()
                index = tmp.read(args.indexfile)
                out['index'] = index
        if args.index:                    
            if 'n' in flags:
                index = [int(i) for i in args.index]
                out['index'] = index

        return out

    def _checkArg(self,arg,msg):
        """
        test
        """

        if not arg:
            msg = msg
            raise FileError(msg)
        
    def _initArgs(self):
        """
        test
        """

        message = "Analyzing CafeMol outputs."
        parser = argparse.ArgumentParser(description=message)
        parser.add_argument('calculation_type',nargs='?',type=str,choices=['distance','cmap','com','readframe'],help='choose calculation type.')
        
        parser.add_argument('-f','--inputfile',nargs='?',help='input file name[.dcd,.pdb,ninfo,psf]')
        parser.add_argument('-o','--outputfile',nargs='?',help='output file name [automaticaly set prefix.] ex) filename(.dat)')
        parser.add_argument('-n','--index',nargs='*',help='Integer. ex) -n 1 2 3 4 5 6')
        parser.add_argument('-nf','--indexfile',nargs='?',help='filename. ex) -nf filename[.ndx]')
        
        self.args = parser.parse_args()

        return self.args

def main():
    tmp = CafePy()
    tmp.main()
    
if __name__ == "__main__":
    main()
