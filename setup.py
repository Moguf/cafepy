#!/usr/bin/env python3
# coding:utf-8

import os
import codecs

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()

setup(
    name='CafePy',
    version='0.0.1',
    description='Python Scripts For Analizing CafeMol Data.',
    author='Mogu',
    author_email='kbu94984@gmail.com',
    long_description=read('README.rst'),
    url='https://github.com/Moguf/cafepy',
    license='GPL3.0',
    packages=find_packages(),
    #install_requires=['numpy','scipy','matplotlib'],
    scripts=['cafepy/cmdline.py'],
    entry_points = {
        'console_scripts' : ['cafepy = cafepy.cmdline:main'],
    },
)


