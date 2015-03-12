__author__ = 'Just_CJ'
import re

if __name__ == '__main__':
    num, low, high = map(int, re.split(r'\s+(?!$)', raw_input()))
    A = []; B = []; C = []; D = []
    for i in range(num):
        id, score1, score2 = map(int, re.split(r'\s+(?!$)', raw_input()))
        if score1>=low and score2>= low:
            if score1>=high and score2>=high:
                A.append((id, score1, score2))
            elif score1>=high:
                B.append((id, score1, score2))
            elif score1>=score2:
                C.append((id, score1, score2))
            else:
                D.append((id, score1, score2))

    A.sort(key = lambda x:(x[1]+x[2], x[1], -x[0]), reverse=True)
    B.sort(key = lambda x:(x[1]+x[2], x[1], -x[0]), reverse=True)
    C.sort(key = lambda x:(x[1]+x[2], x[1], -x[0]), reverse=True)
    D.sort(key = lambda x:(x[1]+x[2], x[1], -x[0]), reverse=True)

    print len(A)+len(B)+len(C)+len(D)

    for item in A:
        print item[0], item[1], item[2]

    for item in B:
        print item[0], item[1], item[2]

    for item in C:
        print item[0], item[1], item[2]

    for item in D:
        print item[0], item[1], item[2]

