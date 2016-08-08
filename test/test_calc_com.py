#!/usr/bin/env python3
# coding:utf-8
import sys
import unittest

class TestCalcCOM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.append("../src")
        from calc_com import CalcCOM
        cls.testclass = CalcCOM()
        
    def setUp(self):
        pass
    
    def test_readDcd(self):
        self.testclass.readDCD("test.dcd")
        
        
    def test_readPDB(self):
        pass
        self.testclass.readPDB()
        
    def test_readIndex(self):
        pass

        
    def test_calcCOMfromPDB(self):
        pass
        self.testclass.calcCOMfromPDB()

    def test_calcCOMfromDCD(self):
        self.testclass.readDCD("test.dcd")
        self.testclass.calcCOMfromDCD()
        
    def test_main(self):
        self.testclass.main()

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
