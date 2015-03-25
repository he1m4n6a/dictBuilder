#!/usr/bin/env python

from optparse import OptionParser
from frequency import frequency
from easyDirectory import *

def writeFile(fp, arr):
    for ele in arr:
        if ele != arr[-1:]:
            fp.write(ele+'\n')
        else:
            fp.write(ele)

if __name__=='__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
            help="input file", metavar="FILE")
    parser.add_option("-s", action="store_true", dest="select",
            help="select top number of directory")
    parser.add_option("-c", "--csv", dest="csv",
            help="set input file as csv format", metavar="CSV")
    parser.add_option("-o", "--output", dest="output",
            help="output dirctory file", metavar="FILE")
    parser.add_option("-n", "--num", dest="num",
            help="input number", metavar="NUM")
    
    (options, args) = parser.parse_args()
    
    if options.filename != None and options.select:
        wordArr = []
        resArr = []
        text = open(options.filename, 'r')
        for line in text.readlines():
            if options.csv != None:
                ele = line.split(',')
                for e in ele:
                    wordArr.append(e)
            else:
                wordArr.append(line.strip('\n'))
        
        #judge the num 
        if options.num != None: 
            try:
                resList = frequency(wordArr, int(options.num))
                for l in resList:
                    resArr.append(l[0])
            except:
                parser.error("please input a num")
        else:
            resList = frequency(wordArr, 100)
            for l in resList:
                resArr.append(l[0])
            
        if options.output != None:
            fp = open(options.output, 'w+')
            writeFile(fp, resArr)
            fp.close()
        else:
            fp = open("output.txt", "w+")
            writeFile(fp, resArr)
            fp.close()
        
    elif options.filename != None:
        pass
