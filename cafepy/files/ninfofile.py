#!/usr/bin/env python3
"""
:Editer:  Mogu
:Version: 0.0.1dev
:environment:  Pyton3.5.1

**contains**

* Ninfo: reads or writes dcd-files.

.. note::
    Don't support DNA and RNA ninfo file 
    and Only support a protein with aicg2+ force-field!!

"""

import re
from collections import OrderedDict

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
        # list
        angle_data = ntmp['angle']

        del ntmp['bond'][0]
    
        ntmp.write('out.file')

    *Members* 

    :self.filename:   Native information file name.
    :self.data:   contains native information data from filename.
    :self.keys:  supports interactions type.
    :self.rewords:   for regular expression. "^bond|^angl|^aicg13|^aicgdih|^dihd|^contact"
    :self.\*\*_format:  for reading native information file.
    

    """
    
    def __init__(self, filename):
        self.filename = filename
        self.data = OrderedDict()
        self.keys = ["bond", "angl", "aicg13", "aicgdih", "dihd", "contact"]
        for ikey in self.keys:
            self.data[ikey] = []
        self.rewords = "^" + "|^".join(self.keys)
        """ ''"""
        
        self.bond_format = [int, int, int, int, int, int, int, float, float, float, float, str]
        self.angl_format = [int, int, int, int, int, int, int, int, int,
                             float, float, float, float, str]
        self.aicg13_format = [int, int, int, int, int, int, int, int, int,
                              float, float, float, float, float, str]
        self.dihd_format = [int, int, int, int, int, int, int, int, int, int, int,
                            float, float, float, float, float, str]
        self.aicgdih_format = [int, int, int, int, int, int, int, int, int, int, int,
                              float, float, float, float, float, str]
        self.contact_format = [int, int, int, int, int, int, int, float, float, int, float, str]
        self._read()
        
        
    def _read(self):
        """
        reads self.filename(ninfo-file) and is called from __init__(filename).

        :input:  None
        :return:  Dictonary data
        
        """
        with open(self.filename, 'r') as fp:
            for iline in fp.readlines():
                pat = re.compile(self.rewords)
                mat = pat.match(iline)
                if mat:
                    if mat.group() == 'bond':
                        idata = [fnc(ele) for ele, fnc in zip(iline.split()[1:], self.bond_format)]
                        """ change str to each format. """
                        self.data['bond'].append(idata)
                    elif mat.group() == 'angl':
                        idata = [fnc(ele) for ele, fnc in zip(iline.split()[1:], self.angl_format)]
                        self.data['angl'].append(idata)
                    elif mat.group() == 'aicg13':
                        idata = [fnc(ele) for ele, fnc in zip(iline.split()[1:], self.aicg13_format)]
                        self.data['aicg13'].append(idata)
                    elif mat.group() == 'dihd':
                        idata = [fnc(ele) for ele, fnc in zip(iline.split()[1:], self.dihd_format)]
                        self.data['dihd'].append(idata)
                    elif mat.group() == 'aicgdih':
                        idata = [fnc(ele) for ele, fnc in zip(iline.split()[1:], self.aicgdih_format)]
                        self.data['aicgdih'].append(idata)
                    elif mat.group() == 'contact':
                        idata = [fnc(ele) for ele, fnc in zip(iline.split()[1:], self.contact_format)]
                        self.data['contact'].append(idata)
        return self.data

    def write(self):
        pass
    
    def __getitem__(self, key):
        return self.data[key]

    def __str__(self, key):
        return self.data.keys()
    
    def close(self):
        pass

    
