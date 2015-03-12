__author__ = 'Just_CJ'

import re

def max_N(num):
    sum = 1
    i=1
    while(sum<=num):
       if (sum+2*(i+2)) > num:
           return (i, num-sum)
       else:
           i+=2
           sum+=2*i

if __name__ == '__main__':
    num, symbol = re.split(r'\s+(?!$)', raw_input())
    num = int(num)
    N, left = max_N(num)
    for i in range((N+1)/2, 0, -1):
        print ((N+1)/2-i)*' '+(2*i-1)*symbol
    for i in range(2, (N+1)/2+1, 1):
        print ((N+1)/2-i)*' '+(2*i-1)*symbol

    print left