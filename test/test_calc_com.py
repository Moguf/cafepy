#!/usr/bin/env python3
# coding:utf-8
import sys
import unittest
from test_data_in_calc_com import *

class TestCalcCOM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from cafepy import CalcCOM
        cls.testclass = CalcCOM()
        
    def setUp(self):
        pass
    
    def test_readDcd(self):
        self.testclass.readDCD("test.dcd")
        
        
    def test_readPDB(self):
        pass
        self.testclass.readPDB()
        
    def test_readIndex(self):
        pass

        
    def test_calcCOMfromPDB(self):
        pass
        self.testclass.calcCOMfromPDB()

    def test_calcCOMfromDCD(self):
        self.testclass.readDCD("test.dcd")
        self.testclass.calcCOMfromDCD()
        self.assertEqual(self.testclass.com.tolist(),center_of_mass_trajectory_test_data)
        self.testclass.close()
        
    def test_calcCOMfromDCD_with_index(self):
        self.testclass.readDCD("test.dcd")
        self.testclass.calcCOMfromDCD([1,2,3,4,5])
        self.assertEqual(self.testclass.com.tolist(),center_of_mass_trajectory_test_data)
        
    def test_calcCOMfromDCD_with_slices(self):
        pass

    def test_calcCOMfromDCD_with_index_and_slices(self):
        pass
        
    def test_main(self):
        self.testclass.main()

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
