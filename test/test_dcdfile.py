#!/usr/bin/env python3
# coding:utf-8

import os
import sys
import unittest

from unittest.mock import patch

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)

from cafepy.files import DCD


class TestReadDcd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        testdata = os.path.join(os.path.dirname(__file__), 'data/test.dcd')
        cls.listdata = os.path.join(os.path.dirname(__file__), 'data/')
        cls.dcd = DCD(testdata)
        sys.path.append(cls.listdata)
        
        from test_data_in_dcdfile import initial_cordinates_of_test_data, final_cordinates_of_test_data, four_trajectories
        cls.initcoord = initial_cordinates_of_test_data
        cls.lastcoord = final_cordinates_of_test_data
        cls.fourcoords = four_trajectories

    def test_readHeader(self):
        pass
        
    def test_get_onestep_with_first_index(self):
        self.assertEqual(self.initcoord, self.dcd[0])

    def test_get_onestep_with_last_index(self):
        self.assertEqual(self.lastcoord, self.dcd[-1])
        
    def test_get_length_of_trajectory_with_len(self):
        self.assertEqual(4, len(self.dcd))
        
    def test_get_a_trajectory_in_loop(self):
        for i, xyz in enumerate(self.dcd):
            self.assertEqual(self.fourcoords[i], xyz)
        
    def test_get_trajectory_with_slieces(self):
        self.assertEqual(self.fourcoords[1:3], self.dcd[1:3])
        
    def test_write_pdb_format(self):
        #self.dcd.write("test_from_dcdfile.pdb", 1, "pdb")
        pass

    def test_make_pdb_from_dcd(self):

        pass
    
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
        #cls.testclass.close()

if __name__ == "__main__":
    unittest.main()
