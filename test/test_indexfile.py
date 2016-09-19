#!/usr/bin/env python3
# coding:utf-8
"""
###  Editer:Mogu  ###
This class read index-file

environment:
    Pyton3.5.1
requirement:

"""
import os
import sys
import unittest

from .test_base import CafePyTestBase


class TestReadIndex(CafePyTestBase):
    @classmethod
    def setUpClass(cls):
        from cafepy.files import Index
        cls.icls = Index(cls.data_path + 'test_index.ndx')
        
    def setUp(self):
        pass

    def test_read_index_file(self):
        self.assertEqual(self.icls.data, [0, 1, 2, 3, 4, 5, 6, 7, 8, 99, 10, 9, 1999])
        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()
