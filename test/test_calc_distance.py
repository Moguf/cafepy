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
        cls.testpath = os.path.join(os.path.dirname(__file__), 'data/test.dcd')
    
    def setUp(self):
        pass

    def test_init_func(self):
        cdist = CalcDistance(self.testpath)
    
    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    

if __name__ == "__main__":
    unittest.main()
