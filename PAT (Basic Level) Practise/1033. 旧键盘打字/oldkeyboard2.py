__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    badkeys = raw_input()
    input = raw_input()
    res = ''
    for ch in input:
        if ch.upper() not in badkeys:
            if '+' in badkeys and ch.isupper():
                continue
            else:
                res += ch

    print res