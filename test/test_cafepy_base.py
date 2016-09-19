import os
import sys
import unittest

from .test_base import CafePyTestBase

from cafepy.utils import CafePyBase

class TestCafePyBase(CafePyTestBase):
    @classmethod
    def setUpClass(cls):
        cls.tcls = CafePyBase()
        
    def setUp(self):
        pass

    def test_read_dcd(self):
        data = self.tcls.read(self.data_path + "test.dcd")
    def test_read_pdb(self):
        data = self.tcls.read(self.data_path + "test.pdb")

    def test_read_ninfo(self):
        data = self.tcls.read(self.data_path + "test.ninfo")

    def test_read_index(self):
        data = self.tcls.read(self.data_path + "test_index.ndx")
    
    
    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

    
