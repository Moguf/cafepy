#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest

from test_base import CafePyTestBase

from cafepy.core.calc_distance import CalcDistance

class TestCalcDistance(CafePyTestBase):
    @classmethod
    def setUpClass(cls):
        cls._set_data_path(cls)
        cls._set_path(cls)
        cls.dcd = cls.data_path + 'test.dcd'
        cls.pdb = cls.data_path + 'test.pdb'
        cls.ndx = cls.data_path + 'test_index.ndx'
        from test_data_in_calc_distance import four_dist_data
        cls.fdist = four_dist_data
        
    def setUp(self):
        pass

    def test_calc_distance_from_dcd(self):
        self.dcls = CalcDistance(self.dcd, self.ndx)
        self.dcls.calcDist()
        self.assertEqual(self.dcls.dist_data, self.fdist)

    def test_calc_distance_from_pdb(self):
        self.dcls = CalcDistance(self.pdb, self.ndx)
        self.assertEqual(self.dcls.calcDist(), [1.5308122027211573,
                                                2.7629712267774345,
                                                2.4108355398077244,
                                                3.015551359204481,
                                                7.581407850788664] )
        
    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    

if __name__ == "__main__":
    unittest.main()
