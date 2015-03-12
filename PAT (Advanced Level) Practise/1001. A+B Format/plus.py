__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    A, B = map(int, re.split('\s+(?!$)', raw_input()))
    res = str(A + B)
    # print res
    ures = res.replace('-', '')

    if len(ures) > 3:
        res_str = ''
    else:
        res_str = ures

    for i in range(len(ures)-3, 0, -3):
        if i > 3:
            res_str =',' + ures[i:i+3] + res_str
        #elif i == 0:
        #    res_str = ures[i:i+3] + res_str
        elif i <= 3:
            res_str = ures[0:i] + ',' + ures[i:i+3] + res_str

    if res[0] == '-':
        res_str = '-' + res_str

    print res_str