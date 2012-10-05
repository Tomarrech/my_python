#coding: utf-8

__author__ = 'Issahar'

inLst = raw_input("Input comma separated numbers: ")

numberList = inLst.split(',')
i = 1
print '# \tID \tNumber'
for val in numberList:
    print i,')\t', val[0:3] ,'\t',val[3:]
    i+=1
raw_input()