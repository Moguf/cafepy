#!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest

class TestCafePy(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        sys.path.append("../src")
        from cafepy import CafePy
        cls.testclass = CafePy()
        cls.initArgs = cls.testclass._initArgs()
        
    def setUp(self):
        pass
        
    def test_with_empty_args(self):
        #with self.assertRaises(SystemExit):
        print(self.initArgs.parse_args([]))
        print(self.initArgs.parse_args(["com","-i test.dcd"]))


    def tearDown(self):
        pass

    

if __name__ == "__main__":
    unittest.main()
