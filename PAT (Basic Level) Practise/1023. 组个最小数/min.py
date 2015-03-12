__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    list = map(int, re.split(r'\s+(?!$)', raw_input()))
    dict = {}
    for i in range(10):
        dict[i] = list[i]

    MSB = min(dict.iteritems(), key = lambda x:(x[1]==0 or x[0]==0, x[0]))[0]
    res = str(MSB)
    dict[MSB] -= 1
    for item in sorted(dict.iteritems(), key = lambda x:x[0]):
        res += str(item[0])*item[1]

    print res