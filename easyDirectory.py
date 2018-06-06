#!/usr/bin/env python
#coding=utf-8

import itertools
import string

res = []
        
#社工字典生成函数
def normalDir(strArr, num):
    for i in range(1, len(strArr)+1):
        for ele in itertools.permutations(strArr, i):
            res.append('%s' %(''.join(ele)))
    return res

#验证码生成函数
def verifyDir(strArr, num):
    for ele in itertools.product(strArr, repeat=num):
        res.append('%s' %(''.join(ele)))
    return res
