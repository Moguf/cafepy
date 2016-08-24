#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest

from unittest.mock import patch

from test_data_in_read_pdb import *

class TestReadDcd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from cafepy import ReadPDB
        cls.testclass = ReadPDB()
        test_inpufile = "test.pdb"
        cls.testclass.openFile(test_inpufile,mode="r")
        
    def test_readPDB(self):
        row_data = self.testclass.readPDB()
        self.assertEqual(row_data,list_pdb_data)
        self.assertEqual(self.testclass[:],list_pdb_coard)
        self.assertEqual(self.testclass[0],self.testclass[:][0])

    def test_len(self):
        self.testclass.readPDB()
        self.assertEqual(873,len(self.testclass))
        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()
