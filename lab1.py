#coding: 866

__author__ = 'Issahar'

inLst = raw_input('Введите номера телефонов через запятую: ')

numberList = inLst.split(',')
i = 1
print '№ \tкод \tномер'
for val in numberList:
    val = eval(val)
    print i,')\t', str(val)[0:3] ,'\t',str(val)[3:] ,'\t'
    i+=1
raw_input()