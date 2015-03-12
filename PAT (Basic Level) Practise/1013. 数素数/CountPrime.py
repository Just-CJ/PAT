__author__ = 'Just_CJ'

import math
import re

def prime(i):
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0: return False
    return True

if __name__ == '__main__':

    start, end = map(int, re.split(r'\s+(?!$)', raw_input()))
    cur = 2
    i = 3
    prime_list = []
    if start == 1:
        prime_list.append(2)
    while cur <= end:
        if prime(i):
            if cur >= start:
                prime_list.append(i)
            cur += 1
        i += 2

    for i in range(len(prime_list)):
        if (i+1)%10 == 0:
            print prime_list[i]
        else:
            print prime_list[i],