__author__ = 'Just_CJ'
import math


def prime(i):
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0: return False
    return True

if __name__ == '__main__':
    num = int(raw_input())
    num_pair = 0
    for i in range(3, num+1, 2):
        if prime(i) and prime(i+2) and i+2<=num:
            num_pair += 1
    print num_pair