__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    num = raw_input()
    dict = {}
    for i in range(10):
        dict[i] = len(re.findall(str(i), num))
        if dict[i] != 0:
            print str(i)+':'+str(dict[i])

