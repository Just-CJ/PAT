__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    num = int(raw_input())
    dict = {0:'1', 1:'0', 2:'X', 3:'9', 4:'8', 5:'7', 6:'6', 7:'5', 8:'4', 9:'3', 10:'2'}
    list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    pass_num = 0
    for i in range(num):
        id = raw_input()
        sum = 0
        cur_pass = True
        for j in range(17):
            if not id[j].isdigit():
                print id
                cur_pass = False
                break
            sum += list[j]*int(id[j])
        if not cur_pass: continue
        if dict[sum%11] == id[17]:
            pass_num += 1
        else:
            print id
    if pass_num == num:
        print 'All passed'

