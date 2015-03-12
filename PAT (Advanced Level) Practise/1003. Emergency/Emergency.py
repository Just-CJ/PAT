__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    city_num, path_num, C1, C2 = map(int, re.split('\s+(?!$)', raw_input()))
    city_rts = map(int, re.split('\s+(?!$)', raw_input()))
    path = {}
    vertex = {}
    for i in range(path_num):
        c1, c2, dis = map(int, re.split('\s+(?!$)', raw_input()))
        path[(c1, c2)] = dis
        if vertex.has_key(c1):
            vertex[c1].append(c2)
        else:
            vertex[c1] = [c2]

    shortest = 0
    shortest_num = 0
    rts_all = 0

    for i in vertex[C1]:
        next = i
        while next != C2:
            if vertex.has_key(next):

            else:
