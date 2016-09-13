#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest

from unittest.mock import patch

from test_data_in_read_pdb import *

class TestPDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.append(os.path.abspath("./test"))
        from cafepy import PDB
        test_inpufile = "./test/test.pdb"
        cls.testclass = PDB(test_inpufile)
        
    def test_readPDB_with_index(self):
        row_data = self.testclass.read()
        self.assertEqual(row_data[0],list_pdb_data[0])

        #self.assertEqual(self.testclass[0],self.testclass[:][0])
        
    def test_readPDB_with_slices(self):
        row_data = self.testclass.read()
        self.assertEqual(self.testclass[:2],list_pdb_coard[:2])
        self.assertEqual(self.testclass[2:5],list_pdb_coard[2:5])
        self.assertEqual(self.testclass[2],list_pdb_coard[2])
        
        

    def test_len(self):
        self.testclass.read()
        self.assertEqual(873,len(self.testclass))
        self.assertEqual(len(self.testclass[2:]),len(list_pdb_coard[2:]))
        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()
