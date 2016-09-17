#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest
from importlib import import_module

from unittest.mock import patch

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)
from cafepy.files import PDB

class TestPDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testdata = os.path.join(os.path.dirname(__file__), 'data/test.pdb')
        cls.listdata = os.path.join(os.path.dirname(__file__), 'data/')
        sys.path.append(cls.listdata)
        from test_data_in_pdbfile import list_pdb_data, list_pdb_coord
        cls.pdblist = list_pdb_coord
        
        cls.pdb = PDB(cls.testdata)
        
    def test_readPDB_with_index(self):
        self.assertEqual([15.939, 14.6, -4.238], self.pdb[0])
        
    def test_readPDB_with_terminal_slices(self):
        self.assertEqual(self.pdb[:2], self.pdblist[:2])

    def test_readPDB_with_terminal_slices(self):
        self.assertEqual(self.pdb[1:4], self.pdblist[1:4])

    def test_readPDB_with_terminal_slices(self):
        self.assertEqual(self.pdb[:2], self.pdblist[:2])
        
    def test_readPDB_with_terminal_slices(self):
        self.assertEqual(self.pdb[:2], self.pdblist[:2])
        
        
    def test_len(self):
        self.assertEqual(873, len(self.pdb))

        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

class TestCGPDB(unittest.TestCase):
    pass
    
if __name__ == "__main__":
    unittest.main()
