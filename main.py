#!/usr/bin/env python
#coding=utf-8

import string
from optparse import OptionParser
from frequency import frequency
from social import social
from easyDirectory import *
from judge import *

if __name__=='__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
            help="input file", metavar="FILE")
    parser.add_option("-m", "--mode", dest="mode",
            help="select mode,default=normal", metavar="[normal|verify|frequency|social]")
    parser.add_option("-s", "--string", dest="string",
            help="input string when use verify mode", metavar="STR")
    parser.add_option("-c", "--csv", dest="csv",
            help="set input file as csv format", metavar="CSV")
    parser.add_option("-o", "--output", dest="output",
            help="output dirctory file", metavar="FILE")
    parser.add_option("-n", "--num", dest="num",
            help="input number", metavar="NUM")
    
    (options, args) = parser.parse_args()
    
    
    wordArr = []
    resArr = []
    
    #输入文件并选择整理最常用密码生成字典
    if options.filename != None and options.mode == "frequency":
        text = open(options.filename, 'r')
        wordArr = judgeCsv(options, text)
        resArr = judgeNum(options, wordArr, frequency)
        judgeOut(options, resArr)
    
    #生成验证码字典
    elif options.mode == "verify":
        if options.filename != None:
            text = open(options.filename, 'r')
            wordArr = judgeCsv(options, text)       
        elif options.string != None:
            #根据输入的字符串生成验证码字典
            wordArr = options.string
        else:
            #默认是数字的验证码
            wordArr = string.digits
                    
        resArr = judgeNum(options, wordArr, verifyDir)
        judgeOut(options, resArr)

    #生产辅助社工爆破字典
    elif options.filename != None  and options.mode == "social":
        text = open(options.filename, 'r')
        wordArr = judgeCsv(options, text)                      
        resArr = judgeNum(options, wordArr, social)
        judgeOut(options, resArr)
        

    #生成普通的迭代字典(默认的模式)
    elif options.filename != None or (options.filename != None and options.mode == "normal"):
        text = open(options.filename, 'r')
        wordArr = judgeCsv(options, text)
        resArr = judgeNum(options, wordArr, normalDir)
        judgeOut(options, resArr)

    else:
        parser.error("请输入正确的参数")
