#!/usr/bin/env python3
import os
import sys
import unittest
import subprocess

class CommandLineCafePyTest(unittest.TestCase):

    def setUp(self):
        sys.path.append("../src")
        from cafepy import CafePy
        self.testclass = CafePy()
        self.cmdline_list = ["python3","../src/cafepy.py",""]
        
    def test_command_line_help_discription(self):
        self.cmdline_list[:]
        tmp[2] = "-h"
        cmdlien = " ".join(tmp)
        outputs = subprocess.check_output(cmdline,shell=True)

    def test_command_line_dist_argments(self):
        tmp = self.cmdline_list[:]
        tmp[2] = "dist -a 1 2 3"
        cmdline = " ".join(tmp)
        outputs = subprocess.check_output(cmdline,shell=True)
        
    def test_command_line_cmap_argments(self):
        tmp = self.cmdline_list[:]
        tmp[2] = "dist -p test.pdb"
        cmdline = " ".join(tmp)
        outputs = subprocess.check_output(cmdline,shell=True)
        
    def tearDown(self):

        pass


if __name__ == "__main__":
    unittest.main()#warnings='ignore')


    
