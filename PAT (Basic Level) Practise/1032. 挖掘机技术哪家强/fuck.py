__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    num = int(raw_input())
    dict = {}
    for i in range(num):
        id, score = map(int, re.split(r'\s+(?!$)', raw_input()))
        if dict.has_key(id):
            dict[id] += score
        else:
            dict[id] = score
    max_element =  max(dict.iteritems(), key = lambda x:x[1])
    print max_element[0], max_element[1]