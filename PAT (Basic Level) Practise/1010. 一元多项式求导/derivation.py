__author__ = 'Just_CJ'
import re

if __name__ == '__main__':
    list_in = map(int, re.split(r'\s+(?!$)', raw_input()))
    list_out = []
    for i in range(0, len(list_in), 2):
        if list_in[i+1] != 0 and list_in[i] != 0:
            list_out.append(list_in[i]*list_in[i+1])
            list_out.append(list_in[i+1]-1)

    if len(list_out) != 0:
        for i in list_out:
            print i,
    else:
        print '0 0'