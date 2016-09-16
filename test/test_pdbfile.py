#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest

from unittest.mock import patch

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)
from cafepy.files import PDB

class TestPDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testdata = os.path.join(os.path.dirname(__file__), 'data/test.pdb')
        cls.pdb = PDB(cls.testdata)
        
    def test_readPDB_with_index(self):
        self.assertEqual([15.939, 14.6, -4.238], self.pdb[0])
        
    def test_readPDB_with_slices(self):
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

class TestCGPDB(unittest.TestCase):
    pass
    
if __name__ == "__main__":
    unittest.main()
