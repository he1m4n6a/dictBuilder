#!/usr/bin/env python
#coding=utf-8

from collections import Counter

resArr = []

def frequency(wordArr, num=100):
    '''
    获取使用最频繁的单词
    '''
    sortList = Counter(wordArr).most_common(num)
    for ele in sortList:
        resArr.append(ele[0])       
    return resArr
