 #!/usr/bin/env python3
# coding:utf-8
import os
import sys
import unittest
from importlib import import_module
from unittest.mock import patch

import numpy as np

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)

from cafepy.utils import cafepy_math as cmath

class TestCafepyMath(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.listdata = os.path.join(os.path.dirname(__file__), 'data/')
        sys.path.append(cls.listdata)
        from test_data_in_pdbfile import list_pdb_coord
        cls.coord = list_pdb_coord
        cls.zaxis = [[0., 0., float(i)] for i in range(10)]

    def test_rotation3d_zaixs(self):
        self.assertEqual(self.zaxis, cmath.rotation3D(self.zaxis, 0., 0., np.pi/3))

    def test_rotation3d_xaixs(self):
        print(self.zaxis, cmath.rotation3D(self.zaxis, np.pi/2, 0., 0.))        



if __name__ == '__main__':
    unittest.main()
