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

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)

class TestReadIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from cafepy.files import Index
        cls.indexclass = Index()
        cls.testpath = os.path.join(os.path.dirname(__file__), 'data/test_index.ndx')
        
    def setUp(self):
        pass

    def test_read_index_file(self):
        data = self.indexclass.read(self.testpath)
        self.assertEqual(data,[0, 1, 2, 3, 4, 5, 6, 7, 8, 99, 10, 9, 1999])
        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()
