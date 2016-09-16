#!/usr/bin/env python3
# fileencoding: utf-8

import os
import sys
import unittest

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)
from cafepy.files import Ninfo

class TestReadNinfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testdata = os.path.join(os.path.dirname(__file__), 'data/test.ninfo')

    def setUp(self):
        pass

    def test_read_bond_from_ninfo_file(self):
        tmp = Ninfo(self.testdata)
        self.assertEqual([1, 1, 1, 1, 2, 1, 2, 3.8223, 1.0, 1.0, 110.4, 'pp'], tmp['bond'][0])
        
    def test_read_angl_from_ninfo_file(self):
        tmp = Ninfo(self.testdata)
        self.assertEqual([1, 1, 1, 1, 2, 3, 1, 2, 3, 131.492, 0.0, 1.0, 0.0, 'ppp'], tmp['angl'][0])

    def test_read_aicg13_from_ninfo_file(self):
        tmp = Ninfo(self.testdata)
        self.assertEqual([1, 1, 1, 1, 2, 3, 1, 2, 3, 6.9701, 1.0, 1.0, 1.3709, 0.15, 'ppp'], tmp['aicg13'][0])
        
    def test_read_dihd_from_ninfo_file(self):
        tmp = Ninfo(self.testdata)
        self.assertEqual([1, 1, 1, 1, 2, 3, 4, 1, 2, 3, 4, -126.5627, 0.0, 1.0, 0.0, 0.0, 'pppp'], tmp['dihd'][0])

    def test_read_aicgdih_from_ninfo_file(self):
        tmp = Ninfo(self.testdata)
        self.assertEqual([1, 1, 1, 1, 2, 3, 4, 1, 2, 3, 4, -126.5627, 1.0, 1.0, 0.435, 0.15, 'pppp'], tmp['aicgdih'][0])

    def test_read_contact_from_ninfo_file(self):
        tmp = Ninfo(self.testdata)
        self.assertEqual([1, 1, 1, 1, 23, 1, 23, 7.2644, 1.0, 1, 0.16, 'p-p'], tmp['contact'][0])
        
        
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
