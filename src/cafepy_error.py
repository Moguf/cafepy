#!/usr/bin/env python3
# coding: utf-8
"""
### Author: Mogu ###
This code is for Errors.

# environment:
    Python3.5.1
# requirements:

"""
class CafePyError(Exception):
    """Base class for exceptions in this module"""
    def __str__(self):
        return self.msg
        
class InputError(CafePyError):
    def __init__(self,expr,msg):
        self.expr = expr
        self.msg = msg

class ReadingError(CafePyError):
    def __init__(self,expr,func,msg):
        self.expr = expr
        self.func = func
        self.msg = msg

class FileError(CafePyError):
    def __init__(self,msg):
        self.msg = msg

class CmdLineError(CafePyError):
    def __init__(self,msg):
        self.msg = msg

        
