.. -*- mode: rst -*-
   
|Travis|_ |Coveralls|_ |Python35| 

.. |Travis| image:: https://travis-ci.org/Moguf/cafepy.svg?branch=master
.. _Travis: https://travis-ci.org/Moguf/cafepy

.. |Coveralls| image:: https://coveralls.io/repos/github/Moguf/cafepy/badge.svg?branch=master
.. _Coveralls: https://coveralls.io/github/Moguf/cafepy?branch=master

.. |Python35| image:: https://img.shields.io/badge/python-3.5-blue.svg

cafepy(Python3 scripts: Under Development)
==========================================

These scripts are for analyzing CafeMol_ outputs.

Requirements
------------

- python3 >= 3.5.1


RECOMMEND
---------

Install virtualenv. (RECOMMEND:for protecting your Home environment.) ::

  python3 -m pip install -U pip setuptools
  python3 -m pip install virtualenv
  # or
  pip3 install virtualenv
  

activate virtualenv::

  virtualenv -p python3 venv
  source venv/bin/activate
  # Removing virtual environment
  # (venv) deactivate 


Set Up
------
::
   
   python3 -m pip install -r requirements.txt
   # or
   pip3 install -r requirements.txt


build & install
---------------
::
   
   cd cafepy
   python3 setup.py build
   python3 setup.py install

   
Example
-------
::

   python3 -m cafepy com -f filename.dcd -o output.file


References
----------
* |CafeMol| CafeMol_ Project.
  
.. _CafeMol: http://www.cafemol.org
.. |CafeMol| image:: http://www.cafemol.org/image/favicon.gif
