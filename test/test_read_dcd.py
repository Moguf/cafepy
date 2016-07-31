#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest

from unittest.mock import patch


class TestReadDcd(unittest.TestCase):
    def setUp(self):
        sys.path.append("../src")
        from read_dcd import ReadDCD
        self.testclass = ReadDCD()
        test_inpufile = "test.dcd"
        self.testclass.openFile(test_inpufile,mode="rb")
        
    def test_readHeader(self):
        self.testclass.readHeader()
        

    def test_get_onestep_wiht_index(self):
        self.testclass[0]

    def test_get_trajectory_with_slieces(self):
        pass

    def test_get_atom_xyz_with_2d_index(self):
        pass
        
    def tearDown(self):
        pass

    def test_readDCD(self):
        pass

if __name__ == "__main__":
    unittest.main()
