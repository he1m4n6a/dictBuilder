#!/usr/bin/env python

import itertools
import string

res = []

class EasyDirectory:
    def __init__(self, strArr, num):
        self.strArr = strArr
        self.num = num
        
    def socialDir(self, strArr):
        for i in range(1, len(arr)+1):
            for ele in itertools.permutations(strArr, i):
                res.append('%s\n' %(''.join(ele)))
                return res
    
    def usualDir(self, strArr, num):
        for ele in itertools.product(strArr, repeat=num):
            res.append('%s\n' %(''.join(ele)))
            return res
