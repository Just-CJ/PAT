__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    A, B = re.split(r'E', raw_input())
    B = int(B)
    digit_num = len(A)-A.index('.')-1
    if B > 0:
        if B < digit_num:
            A = A.replace(A[A.index('.'):A.index('.')+B+1], A[A.index('.')+1:A.index('.')+B+1]+'.')
        else:
            A = A.replace('.', '')
            A += '0'*(B-digit_num)
        print A.replace('+', '')

    elif B == 0:
        print A.replace('+', '')

    else:
        A = A.replace('.', '')
        A_N = A[0]+'0.'+'0'*(-B-1)+A[1:]
        print A_N.replace('+', '')