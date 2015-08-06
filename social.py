#!/usr/bin/env python
#coding=utf-8

resArr = []

#社工字典生成
def social(wordArr):
    for ele in wordArr:
        ele = ele.strip('\n').strip('\r')
        with open('weak.txt','r') as f:
            for item in f.readlines():
                s = item.replace('{user}', ele)
                resArr.append(s.strip('\n'))
            f.seek(0)
    return resArr
