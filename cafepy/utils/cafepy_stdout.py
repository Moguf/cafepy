#!/usr/bin/env python3
# coding:utf-8
"""
### Author: Mogu ###
This file contains a class which show an animation in stdout during Caluclaing.

# Environment:
    Python3.5.1
# Requirements:

# References:
    1) in Ch18,"Fluent Python" [By Luciano Ramalho], 2015.

"""
import sys
import time
import threading
import itertools


class Signal:
    go = True


class CafepyStdout:
    def __init__(self):
        self.duration_time = 0
        self.signal = Signal()
        
    def start(self):
        msg = "Caluclating->\t: "
        self.spinner = threading.Thread(target=self.spin,args=(msg,self.signal))
        self.spinner.start()

    def spin(self,msg,signal):
        # Show Spin.
        spins  = '|/-\\'
        spins2 = '/-\\|'
        spins3 = '-\\|/'
        spins4 = '\\|/-'
        sys.stdout.write(msg)
        for i in itertools.cycle(range(4)):
            out = "\t{}{}{}{}".format(spins[i],spins2[i],spins3[i],spins4[i])
            sys.stdout.write(out)
            sys.stdout.flush()
            sys.stdout.write('\x08'*len(out))
            time.sleep(.1)
            if not signal.go:
                break
        sys.stdout.write('\x08'*(4+len(msg)))
        
    def end(self):
        self.signal.go = False
        self.spinner.join()

    
if __name__ == '__main__':
    import time    
    tmp = CafepyStdout()
    tmp.start()
    tmp.end()
