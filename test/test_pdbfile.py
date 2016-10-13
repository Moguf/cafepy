#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest
from importlib import import_module

from unittest.mock import patch

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)
from cafepy.files import PDB, CGPDB

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

    def test_readPDB_with_terminal_slices1(self):
        self.assertEqual(self.pdb[1:4], self.pdblist[1:4])

    def test_readPDB_with_terminal_slices2(self):
        self.assertEqual(self.pdb[:-1], self.pdblist[:-1])
        
    def test_readPDB_with_terminal_slices3(self):
        self.assertEqual(self.pdb[::], self.pdblist[::])
        
        
    def test_len(self):
        self.assertEqual(873, len(self.pdb))

        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

class TestCGPDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testdata = os.path.join(os.path.dirname(__file__), 'data/cgtest.pdb')
        cls.listdata = os.path.join(os.path.dirname(__file__), 'data/')
        sys.path.append(cls.listdata)
        cls.cgpdb = CGPDB(cls.testdata)

    def tearDown(self):
        pass

    def test_read_cgpdb(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass


    
if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestPDB)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCGPDB)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
