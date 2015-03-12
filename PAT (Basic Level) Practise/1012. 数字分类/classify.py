__author__ = 'Just_CJ'
import re
import math

if __name__ == '__main__':
    list_in = map(int, re.split(r'\s+(?!$)', raw_input()))

    A1 = []; A2 = []; A3 = []; A4 = []; A5 = []

    for i in range(1, list_in[0]+1):
        if list_in[i]%5 == 0 and list_in[i]%2 == 0:
            A1.append(list_in[i])
        elif list_in[i]%5 == 1:
            A2.append(list_in[i]*int(math.pow(-1, len(A2))))
        elif list_in[i]%5 == 2:
            A3.append(list_in[i])
        elif list_in[i]%5 == 3:
            A4.append(list_in[i])
        elif list_in[i]%5 == 4:
            A5.append(list_in[i])

    if len(A1) == 0:
        print 'N',
    else:
        print sum(A1),

    if len(A2) == 0:
        print 'N',
    else:
        print sum(A2),

    if len(A3) == 0:
        print 'N',
    else:
        print len(A3),

    if len(A4) == 0:
        print 'N',
    else:
        print '%.1f' % (float(sum(A4))/len(A4)),

    if len(A5) == 0:
        print 'N',
    else:
        print max(A5),