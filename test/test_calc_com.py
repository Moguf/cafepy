#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)

from cafepy.core import CalcCOM

class TestCalcCOM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testpath = os.path.join(os.path.dirname(__file__), 'data/test.dcd')
        listpath = os.path.join(os.path.dirname(__file__), 'data/')
        cls.com = CalcCOM(cls.testpath)
        sys.path.append(listpath)
        from test_data_in_calc_com import center_of_mass_trajectory_test_data ,\
            center_of_mass_trajectory_test_data_5_atoms
        
        cls.com_data = center_of_mass_trajectory_test_data
        cls.com_5_atoms = center_of_mass_trajectory_test_data_5_atoms
    def setUp(self):
        pass
        
    def test_readPDB(self):
        pass

        
    def test_readIndex(self):
        pass
        
    def test_calc_com_from_dcd(self):
        com = CalcCOM(self.testpath)
        com.run()
        self.assertEqual(com.com.tolist(), self.com_data)
        com.close()
        
    def test_run_with_indexes_from_dcd(self):
        com = CalcCOM(self.testpath)        
        com.run([1,2,3,4,5])
        self.assertEqual(com.com.tolist(), self.com_5_atoms)
        com.close()
        
    def test_calcCOMfromDCD_with_range(self):
        com = CalcCOM(self.testpath)        
        com.run(range(1,6))
        self.assertEqual(com.com.tolist(), self.com_5_atoms)
        com.close()
        

    def test_calcCOMfromDCD_with_index_and_slices(self):
        pass
        
    def test_main(self):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
