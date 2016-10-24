#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest
from importlib import import_module

from unittest.mock import patch

from .test_base import CafePyTestBase

from cafepy.files import PDB, CGPDB

class TestPDB(CafePyTestBase):
    @classmethod
    def setUpClass(cls):
        pass
    
    def setUp(self):
        from test_data_in_pdbfile import list_pdb_data, list_pdb_coord
        self.pdblist = list_pdb_coord
        self.pdb = PDB(self.data_path+'test.pdb')
        
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

class TestCGPDB(CafePyTestBase):
    @classmethod
    def setUpClass(cls):
        pass
    
    def setUp(self):
        self.cgpdb = CGPDB(self.data_path+'cgtest.pdb')
        self.bigpdb = CGPDB(self.data_path+'big_test.pdb')
        
    def test_unit_size_from_bigpdb(self):
        self.assertEqual(self.bigpdb.info['usize'], 60)

    def test_unit_size_from_cgpdb(self):
        self.assertEqual(self.cgpdb.info['usize'], 1)

    def test_amino_acid_size_from_bigpdb(self):
        self.assertEqual(self.cgpdb.info['aasize'], 56)
        
    def test_amino_acid_size_from_bigpdb(self):
        self.assertEqual(self.bigpdb.info['aasize'], [587 for i in range(60)])
        
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
