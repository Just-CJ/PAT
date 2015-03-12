__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    A, B, D = map(int, re.split(r'\s+(?!$)', raw_input()))
    plus = A+B
    res = ''
    while plus >= D:
        res = str(plus % D) + res
        plus /= D

    res = str(plus) + res
    print res