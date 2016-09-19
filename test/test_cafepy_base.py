import os
import sys
import unittest

from test_utils import set_path, set_data_path

set_path()

from cafepy.utils import CafePyBase

class TestCafePyBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tcls = CafePyBase()
        cls.datapath = set_data_path()
        
    def setUp(self):
        pass

    def test_read_dcd(self):
        data = self.tcls.read(self.datapath + "test.dcd")

    def test_read_pdb(self):
        data = self.tcls.read(self.datapath + "test.pdb")

    def test_read_ninfo(self):
        data = self.tcls.read(self.datapath + "test.ninfo")

    def test_read_index(self):
        data = self.tcls.read(self.datapath + "test_index.ndx")
    
    
    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

    
