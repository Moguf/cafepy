#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest

from .test_base import CafePyTestBase

class TestCalcDistance(CafePyTestBase):
    @classmethod
    def setUpClass(cls):
        from cafepy.core.calc_distance import CalcDistance
        cls._set_data_path(cls)        
        cls.tcls = CalcDistance(cls.data_path + 'test.dcd')
        
    def setUp(self):
        pass

    def test_init_func(self):
        pass
    
    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    

if __name__ == "__main__":
    unittest.main()
