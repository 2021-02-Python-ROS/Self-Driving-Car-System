#!/usr/bin/env python

import abc

class ScanMethod:
    __mataclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def do_behavior(self):
        raise NotImplementedError()
