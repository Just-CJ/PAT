__author__ = 'Just_CJ'
import re
if __name__ == '__main__':
    num = int(raw_input())
    for i in range(num):
        A, B, C = map(int, re.split(r'\s+(?!$)', raw_input()))
        print 'Case #'+str(i+1)+': '+str(A+B>C).lower()
