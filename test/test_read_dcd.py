#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest

from unittest.mock import patch

from test_data import *

class TestReadDcd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.append("../src")
        from read_dcd import ReadDCD
        cls.testclass = ReadDCD()
        test_inpufile = "test.dcd"
        cls.testclass.openFile(test_inpufile,mode="rb")

    def test_readHeader(self):
        self.testclass.readHeader()

    def test_get_onestep_wiht_index(self):
        self.testclass.readHeader()
        self.assertEqual(initial_cordinates_of_test_data,self.testclass[0])
        ## check initianl_cordinate
        self.assertEqual(final_cordinates_of_test_data,self.testclass[2999])
        ## check final_cordinate
        

    def test_get_length_of_trajectory_with_len(self):
        self.testclass.readHeader()
        self.assertEqual(3001,len(self.testclass))
        self.testclass._header.tstep = 3
        self.assertEqual(3001,len(self.testclass))
        
    def test_get_a_trajectory_in_loop(self):
        self.testclass.readHeader()
        #for i in self.testclass[2:3]:
        #    print(i)
        
    def test_get_trajectory_with_slieces(self):
        self.testclass.readHeader()
        print(self.testclass[2:5])
        #print(self.testclass[2::2])
        #print(self.testclass[2::2])
        #print(self.testclass[-2:-4])

    def test_readDCD(self):
        pass
    
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()
