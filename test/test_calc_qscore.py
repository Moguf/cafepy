#!/usr/bin/env python3
# fileencoding:utf-8
import os
import sys
import unittest

from .test_base import CafePyTestBase


class TestCalcQscore(CafePyTestBase):
    @classmethod
    def setUpClass(cls):
        from cafepy.core.calc_qscore import CalcDistance
        cls._set_data_path(cls)
        dcd = cls.data_path + 'test.dcd'
        ndx = cls.data_path + 'test_index.ndx'
        cls.dcls = CalcDistance(dcd, ndx)
        
    def setUp(self):
        pass

    def test_read_files(self):
        print('>>>>')
        print(self.dcls.data[:])

    
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
