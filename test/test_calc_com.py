#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest

import numpy

from cafepy.core import CalcCOM

from .test_base import CafePyTestBase

class TestCalcCOM(CafePyTestBase):
    @classmethod
    def setUpClass(cls):
        pass
        
    def setUp(self):
        from test_data_in_calc_com import center_of_mass_trajectory_test_data ,\
            center_of_mass_trajectory_test_data_5_atoms
        self.com_data = center_of_mass_trajectory_test_data
        self.com_5_atoms = center_of_mass_trajectory_test_data_5_atoms

        self.dcd = self.data_path+'test.dcd'
        self.pdb = self.data_path+'test.pdb'
        self.cgpdb = self.data_path+'cgtest.pdb'
        self.bpdb = self.data_path+'big_test.pdb'                        


    def test_readPDB(self):
        com = CalcCOM(self.pdb)
        com.run()
        ans = [17.16436541,   3.21423024,  -4.56492325]
        for x, a in zip(com.com, ans):
            self.assertAlmostEqual(x, a)        

    def test_readBigPDB(self):
        com = CalcCOM(self.bpdb)
        
    def test_readCGPDB(self):
        com = CalcCOM(self.cgpdb)
        
    def test_readIndex(self):
        pass
        
    def test_calc_com_from_dcd(self):
        com = CalcCOM(self.dcd)
        com.run()
        self.assertEqual(com.com.tolist(), self.com_data)
        com.close()
        
    def test_run_with_indexes_from_dcd(self):
        com = CalcCOM(self.dcd)        
        com.run([1,2,3,4,5])
        self.assertEqual(com.com.tolist(), self.com_5_atoms)
        com.close()
        
    def test_calcCOMfromDCD_with_range(self):
        com = CalcCOM(self.dcd)        
        com.run(range(1,6))
        self.assertEqual(com.com.tolist(), self.com_5_atoms)
        com.close()
        
    def test_calcCOMfromDCD_with_index_and_slices(self):
        pass
        
    def test_calc_com_from_cgpdb_with_unit_indexes(self):
        com = CalcCOM(self.bpdb)
        com.run(unit_idx=[1])
        ans = [-42.01642589, 15.75263203, 95.42158773]
        for x, a in zip(com.com, ans):
            self.assertAlmostEqual(x, a)        


    def test_calc_com_from_cgpdb_with_atom_indexes(self):
        com = CalcCOM(self.bpdb)
        com.run(atom_idx=[0,1])
        ans = [ 27.2185, 17.1195, 57.5215]
        for x, a in zip(com.com, ans):
            self.assertAlmostEqual(x, a)        
            
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
