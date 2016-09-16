#!/usr/bin/env python3
"""
:Editer:  Mogu
:Version: 0.0.1dev
:environment:  Pyton3.5.1

**contains**

* Ninfo: reads or writes dcd-files.

.. note::
    Don't support DNA and RNA ninfo file.!!

"""

import re


class Ninfo(object):
    """
    Ninfo class provies reading and writing ninfo-file. "Ninfo" stands for Native information. 
    This Information comes from Native Protain structures. For example, it contains disntances beetween a pair of atoms. 

    *The structure of ninfo file*



    :: 

        <<<<
        bond ibd(int) iunit1(int) iunit2(int) Allatom(int) Allatom(int) Unitatom(int) Unitatom(int) \\
             bd_nat(real) factor_bd(real) correct_mgo(real) coef_bd(real) type(char(2))
        ...
        ...
        >>>>
    
        <<<<
        angle ...
        ...
        ...
        >>>>
    
    *Usage in Scripts*
    
    .. code-block:: python
  
        import cafepy.files.Ninfo

        ntmp = Ninfo('test.ninfo')
        print(ntmp)
        # return data from interaction type.
        bond_data = ntmp['bond']
        angle_data = ntmp['angle']

        del ntmp['bond'][0]
    
        ntmp.write('out.file')
    
    """
    
    def __init__(self):
        self.data=OrderedDict()
        for ikey in ["bond", "angl", "aicg13", "aicgdih", "dihd", "contact"]:
            self.data[ikey]=[]


    
