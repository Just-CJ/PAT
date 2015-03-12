__author__ = 'Just_CJ'

import re

def gcd(a, b):
    if a<b: a, b = b, a
    if b== 0:
        return 1
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def makenum(a, b):
    op = ''
    if abs(a)/abs(b) > 0:
        op+=str(abs(a)/abs(b))
        if abs(a)%abs(b) != 0:
            op+=' '+str((abs(a)%abs(b))/gcd(abs(a)%abs(b), abs(b)))+'/'+str(abs(b)/gcd(abs(a)%abs(b), abs(b)))
    elif abs(a)%abs(b) != 0:
        op+=str((abs(a)%abs(b))/gcd(abs(a)%abs(b), abs(b)))+'/'+str(abs(b)/gcd(abs(a)%abs(b), abs(b)))
    else:
        op+='0'
    if a*b < 0:
        op = '(-'+op+')'
    return op

if __name__ == '__main__':
    A, B = re.split(r'\s+(?!$)', raw_input())
    a1, b1 = map(int, A.split('/'))
    a2, b2 = map(int, B.split('/'))
    op1 = makenum(a1, b1)
    op2 = makenum(a2, b2)

    res = makenum(a1*b2+a2*b1, b1*b2)
    print op1, '+', op2, '=', res

    res = makenum(a1*b2-a2*b1, b1*b2)
    print op1, '-', op2, '=', res

    res = makenum(a1*a2, b1*b2)
    print op1, '*', op2, '=', res

    if a2 == 0:
        res = 'Inf'
    else:
        res = makenum(a1*b2, b1*a2)
    print op1, '/', op2, '=', res


