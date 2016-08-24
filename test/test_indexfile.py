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

class TestReadIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from cafepy import Index
        cls.indexclass = Index()
        
    def setUp(self):
        pass

    def test_read_index_file(self):
        ndxfile = "test_index.ndx"
        data = self.indexclass.read(ndxfile)
        self.assertEqual(data,[0, 1, 2, 3, 4, 5, 6, 7, 8, 99, 10, 9, 1999])
        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()
