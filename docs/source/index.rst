.. -*- mode: rst -*-
   
.. CafePy documentation master file, created by
   sphinx-quickstart on Mon Aug 22 15:55:05 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

|Travis|_ |Coveralls|_ |Python35|  |PyPi|_

.. |Travis| image:: https://travis-ci.org/Moguf/cafepy.svg?branch=master
.. _Travis: https://travis-ci.org/Moguf/cafepy

.. |Coveralls| image:: https://coveralls.io/repos/github/Moguf/cafepy/badge.svg?branch=master
.. _Coveralls: https://coveralls.io/github/Moguf/cafepy?branch=master

.. |Python35| image:: https://img.shields.io/badge/python-3.5-blue.svg

.. |PyPi| image:: https://badge.fury.io/py/CafePy.svg                      
.. _PyPi: https://badge.fury.io/py/CafePy

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
- Numpy
- Scipy
- Matplotlib

How to get
^^^^^^^^^^^^

.. code-block:: bash

   git clone https://github.com/Moguf/cafepy.git
   # or
   pip install -U CafePy
   

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

   
Usage
^^^^^^^

*Command Line Usage*

.. code-block:: bash
                
   python3 -m cafepy com -f filename.dcd -o output.file


*Script Usage Samples*

* Read dcd file.

.. code-block:: python

   from cafepy.files import DCD
   dcd = DCD('test.dcd')
   # you can get a coordinate of protein with list format.
   print(dcd[0])
   # you can get a coordinate of 1th atom with list format.
   print(dcd[0][0])
   

* Read Ninfo file.

.. code-block:: python

   from cafepy.files import Ninfo
   
   ntmp = Ninfo('test.ninfo')
   print(ntmp)
   # return data from interaction type.
   bond_data = ntmp['bond']
   # return list format.
   angle_data = ntmp['angle']
   del ntmp['bond'][0]
                
   ntmp.write('out.file')
   # don't support write() yet.
   
   


Other softwares for Analyzing CafeMol Outputs.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can get a lot of information from below.

* Python codes
  
  * https://github.com/mash-it/CafeMolAnalysis
  * https://github.com/naotohori/cafysis

* C++ codes ( faster than python codes )
  
  * https://github.com/noinil/pinang    
  * https://github.com/ToruNiina/Coffee-mill


Other softwares for Analyzing Molecular Dynamics.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* http://www.mdanalysis.org
* http://mdtraj.org
  
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


