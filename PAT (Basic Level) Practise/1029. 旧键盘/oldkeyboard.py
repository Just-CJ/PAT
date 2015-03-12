__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    str_in = raw_input()
    str_out = raw_input()
    broken_list = []
    for i in range(len(str_in)):
        if str_in[i].upper() not in broken_list:
            match = re.search('['+str_in[i].lower()+str_in[i].upper()+']', str_out)
            if not match:
                broken_list.append(str_in[i].upper())
    res = ''
    for item in broken_list:
        res+=item
    print res