#!/usr/bin/env python3
# coding:utf-8
import sys
import unittest

class TestCalcCOM(unittest.TestCase):
    def setUp(self):
        sys.path.append("../src")
        from calc_com import CalcCOM
        self.testclass = CalcCOM()
        
    def test_readDcd(self):
        self.testclass.readDCD()
        

    def test_readPDB(self):
        self.testclass.readPDB()
        
    def test_readIndex(self):
        pass

        
    def test_calcCOMfromPDB(self):
        self.testclass.calcCOMfromPDB()

    def test_calcCOMfromDCD(self):
        self.testclass.calcCOMfromDCD()
        
    def test_main(self):
        self.testclass.main()

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
