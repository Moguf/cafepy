import os
import sys

def set_path():
    """
    To import cafepy
    """
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def set_data_path():
    """
    To open data-file.
    """
    path = os.path.join(os.path.dirname(__file__), 'data/')
    return path
