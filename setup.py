#!/usr/bin/env python3
# coding:utf-8

#from distutils.core import setup
from setuptools import setup

setup(
    name='CafePy',
    version='0.0.1',
    description='Python Scripts For Analizing CafeMol Data.',
    author='Mogu',
    author_email='kbu94984@gmail.com',
    url='',
    packages=['cafepy', 'cafepy.utils', 'cafepy.files', 'cafepy.core'],
    #install_requires=['numpy','scipy','matplotlib'],
    entry_points = {
        'console_scirpts' : ['cafepy=cafepy.cafepy.__main__'],
    }
)
