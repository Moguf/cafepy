#!/usr/bin/env python3
# coding:utf-8

import os
import codecs

from setuptools import setup, find_packages, Extension

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()


mod_qscore = Extension('qscore',
                       sources = ['clib/src/calc_qscore_c.cpp'])

setup(
    name='CafePy',
    version='0.0.1.dev1',
    description='Python Scripts For Analizing CafeMol Outputs.',
    author='Mogu',
    author_email='kbu94984@gmail.com',
    long_description=read('README.rst'),
    url='https://github.com/Moguf/cafepy',
    license='GPL3.0',
    packages=find_packages(),
    install_requires=['numpy','scipy','matplotlib'],
    scripts=['scripts/cmdline.py'],
    entry_points = {
        'console_scripts' : ['cafepy = scripts.cmdline:main'],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    ext_modules=[mod_qscore]
)


