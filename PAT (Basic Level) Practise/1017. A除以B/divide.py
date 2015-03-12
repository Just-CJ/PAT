__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    A, B = re.split(r'\s+(?!$)', raw_input())
    Q = ''
    R = ''
    last = 0
    for i in range(len(A)):
        cur = 10*last + int(A[i])
        Q += str(cur/int(B))
        last = cur%int(B)

    print int(Q), last
