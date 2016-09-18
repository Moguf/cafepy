#!/usr/bin/env python3
# coding:utf-8
import os
import sys

import unittest

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)

from cafepy.core import calcDistance


class TestCalcDistance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testpath = os.path.join(os.path.dirname(__file__), 'data/test.dcd')

    
    def setUp(self):
        pass

    def test_init_func(self):
        cdist = calcDistance(testpath)
    
    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    

if __name__ == "__main__":
    unittest.main()
