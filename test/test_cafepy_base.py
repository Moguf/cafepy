import os
import sys
import unittest

from unittest.mock import patch

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)

from cafepy.files import DCD

class TestCafePyBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

    
