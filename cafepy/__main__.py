#!/usr/bin/env python3
# coding: utf-8
'''
### Author: Mogu ###
This method called from "python3 -m cafepy"

'''
def main():
    """
    :: This method is called form command line. 
    ex)
        python3 -m cafepy
    """
    import os, sys
    from cafepy.cafepy import CafePy
    sys.path.append(os.path.abspath('.'))
    tmp = CafePy()
    tmp.main()
    

if __name__ == '__main__':
    main()
