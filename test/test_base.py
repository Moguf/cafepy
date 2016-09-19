import os, sys, unittest

class CafePyTestBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CafePyTestBase, self).__init__(*args, **kwargs)
        self._set_path()
        self._set_data_path()

    def _set_path(self):
        """
        To import cafepy
        """
        sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
        
    def _set_data_path(self):
        """
        sets test data path.
        """
        self.data_path = os.path.join(os.path.dirname(__file__), 'data/')
        sys.path.append(os.path.join(os.path.dirname(__file__), 'data/'))
        
        
