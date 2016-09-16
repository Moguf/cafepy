.. -*- mode: rst -*-
   
.. CafePy documentation master file, created by
   sphinx-quickstart on Mon Aug 22 15:55:05 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

|Travis|_ |Coveralls|_ |Python35| 

.. |Travis| image:: https://travis-ci.org/Moguf/cafepy.svg?branch=master
.. _Travis: https://travis-ci.org/Moguf/cafepy

.. |Coveralls| image:: https://coveralls.io/repos/github/Moguf/cafepy/badge.svg?branch=master
.. _Coveralls: https://coveralls.io/github/Moguf/cafepy?branch=master

.. |Python35| image:: https://img.shields.io/badge/python-3.5-blue.svg

Welcome to CafePy's documentation!
==================================
                      

cafepy(Python3 scripts: Under Development)
------------------------------------------
                      
This CafePy is a tool for analyzing `CafeMol`_ outputs. `CafeMol`_ is one of the greatest Molecluar Dynamics simulation Software. The software provides a large time scale and a big structure scale simulation by using Coarse-Grained methods.

CafePy provides ..

* Reading some files [PDB, DCD, NINFO]
* calcurating Center of Mass from [PDB, DCD]
* .. Now under development.

Requirements
^^^^^^^^^^^^

- python3 >= 3.5.1


RECOMMEND
^^^^^^^^^^^^

Install virtualenv. (RECOMMEND:for protecting your Home environment.)

.. code-block:: bash
                
  python3 -m pip install -U pip setuptools
  python3 -m pip install virtualenv
  # or
  pip3 install virtualenv
  
activate virtualenv

.. code-block:: bash
                
  virtualenv -p python3 venv
  source venv/bin/activate
  # Removing virtual environment
  # (venv) deactivate 


Set Up
^^^^^^^^^^^^

.. code-block:: bash
                
   python3 -m pip install -r requirements.txt
   # or
   pip3 install -r requirements.txt


*build & install*


.. code-block:: bash
                
   cd cafepy
   python3 setup.py build
   python3 setup.py install
   
   ## or

   cd cafepy
   pip3 install -e .


Documentation
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   cd cafepy/docs
   make html

   
Example
^^^^^^^

*Command Line Usage*


.. code-block:: bash
                
   python3 -m cafepy com -f filename.dcd -o output.file


*Script Usage Samples*


.. code-block:: python

   import cafepy
                
   


Other softwares for Analyzing CafeMol .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can get a lot of information from below.

* https://github.com/ToruNiina/Coffee-mill
* https://github.com/mash-it/CafeMolAnalysis
* https://github.com/noinil/pinang  
* https://github.com/naotohori/cafysis
  

Code Documentation.
^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1
              
   cafepy

   
References
^^^^^^^^^^^^^

* CafeMol_ Project.
  
.. _CafeMol: http://www.cafemol.org
  
   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


