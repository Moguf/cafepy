#!/usr/bin/env python3
# coding:utf-8
import sys
import unittest

class TestCalcCOM(unittest.TestCase):
    def setUp(self):
        sys.path.append("../src")
        from calc_com import CalcCOM

    def test_readDcd(self):
        pass

    def test_readPdb(self):
        pass

    def test_calcCOMfromPDB(self):
        pass

    def test_calcCOMfromDCD(self):
        pass
        
    def test_main(self):
        pass


        
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
