#!/usr/bin/env python
#coding=utf-8

from optparse import OptionParser

#写入文件函数
def writeFile(fp, arr):
    for ele in arr:
        if ele != arr[-1:]:
            fp.write(ele+'\n')
        else:
            fp.write(ele)

#判断是否选择csv文件格式
def judgeCsv(options, text):
    wordArr = []
    for line in text.readlines():
        if options.csv != None:
            ele = line.split(',')
            for e in ele:
                wordArr.append(e)
        else:
            wordArr.append(line.strip('\n'))        
    return wordArr
    
#判断是否为数字
def judgeNum(options, wordArr, func):
    resArr = []
    if options.num != None: 
        try:
            resArr = func(wordArr, int(options.num))
            return resArr
        except:
            exit("error:请输入一个数字")
    else:
        if func.__name__ == "social":
            resArr = func(wordArr)
        elif func == "frequency":
            resArr = func(wordArr, 100)
        else:
            resArr = func(wordArr, 4)
    return resArr
    
#判断是否输入文件名 
def judgeOut(options, resArr):
    if options.output != None:
        fp = open(options.output, 'w+')
        writeFile(fp, resArr)
        fp.close()
    else:
        fp = open("output.txt", "w+")
        writeFile(fp, resArr)
        fp.close()
