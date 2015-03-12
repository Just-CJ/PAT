__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    list1 = map(float, re.split('\s+(?!$)', raw_input()))
    list2 = map(float, re.split('\s+(?!$)', raw_input()))

    poly = {}

    for i in range(int(list1[0])):
        poly[int(list1[1+2*i])] = list1[2+2*i]

    for i in range(int(list2[0])):
        if poly.has_key(int(list2[1+2*i])):
            poly[int(list2[1+2*i])] += list2[2+2*i]
            if poly[int(list2[1+2*i])] == 0.0:
                poly.pop(int(list2[1+2*i]))
        else:
            poly[int(list2[1+2*i])] = list2[2+2*i]

    res = sorted(poly.iteritems(), reverse=True)

    print len(res),
    for item in res:
        print item[0],
        print '%.1f' % item[1],