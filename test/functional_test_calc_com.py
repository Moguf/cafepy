#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest
import subprocess

class CommandLineCalcCOMTest(unittest.TestCase):
    def setUp(self):
        sys.path.append("../src")
        from cafepy import CafePy
        self.testclass = CafePy()
        self.cmdline_list = ["python3","../src/cafepy.py",""]
        
    def test_command_line_COM_argments(self):
        tmp = self.cmdline_list[:]
        tmp[2] = "com -i test.dcd"
        cmdline = " ".join(tmp)
        outputs = subprocess.check_output(cmdline,shell=True)
        
    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()#warnings='ignore')
