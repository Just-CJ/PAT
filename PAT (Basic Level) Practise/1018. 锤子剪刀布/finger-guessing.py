__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    num = int(raw_input())
    win = 0
    draw = 0
    lose = 0
    dict_A = {'B':0, 'C':0, 'J':0}
    dict_B = {'B':0, 'C':0, 'J':0}
    for i in range(num):
        A, B = re.split(r'\s+(?!$)', raw_input())
        if A==B:
            draw += 1
        elif (A=='C' and B=='J') or (A=='J' and B=='B') or (A=='B' and B=='C'):
            win += 1
            dict_A[A] += 1
        else:
            lose += 1
            dict_B[B] += 1

    print win, draw, lose
    print lose, draw, win
    #print dict_A
    #print dict_B
    print min(dict_A.items(), key = lambda x:(-x[1], x[0]))[0],
    print min(dict_B.items(), key = lambda x:(-x[1], x[0]))[0]


