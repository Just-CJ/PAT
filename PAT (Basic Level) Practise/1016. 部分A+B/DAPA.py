__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    A, DA, B, DB = map(str, re.split(r'\s+(?!$)', raw_input()))
    if re.search(DA, A):
        PA = int(''.join(re.findall(DA, A)))
    else:
        PA = 0
    if re.search(DB, B):
        PB = int(''.join(re.findall(DB, B)))
    else:
        PB = 0

    print PA+PB

