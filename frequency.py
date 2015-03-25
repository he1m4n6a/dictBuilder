#!/usr/bin/env python

from collections import Counter

sortlist = []

def frequency(wordArr, num=100):
    '''
    get the most frequency word
    '''
    sortlist = Counter(wordArr).most_common(num)
    return sortlist
