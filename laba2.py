#coding:UTF8
__author__ = 'Issahar'

import math
import random

def get_data():
    data=[]
    data.append((random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)))
    return data

if __name__ == '__main__':
    for i in range(10):
        Numbers = get_data()
        print Numbers

        for x1,x2,x3,x4 in Numbers:
            y = (math.log(x1+x2)/math.log(3))/(math.log(x3)/math.log(2+x4))
            print 'y(',i +1,')=', y