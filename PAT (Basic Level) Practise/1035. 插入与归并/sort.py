__author__ = 'Just_CJ'

import re

def insert(i, insert_num, res):
    sorted_list = res[0:i]
    sorted_list.append(insert_num)
    sorted_list.sort()
    res2 = sorted_list + res[i+1:len(res)]
    return res2


def merge(list):
    res = []
    for i in range(0, len(list), 2):
        if i+1 != len(list):
            item = list[i]+list[i+1]
            item.sort()
            res.append(item)
        else:
            res.append(list[i])
    return res

def make_list(merge_list):
    res = []
    for list in merge_list:
        res += list
    return res

if __name__ == '__main__':
    num = int(raw_input())
    input_list = map(int, re.split(r'\s+(?!$)', raw_input()))
    #insertion_sort(input_list)
    some_list = map(int, re.split(r'\s+(?!$)', raw_input()))
    res_insert = input_list[:]
    for i in range(1, num):
        res_insert = insert(i, input_list[i], res_insert)
        #print res_insert
        if res_insert == some_list and i!=(num-1):
            print 'Insertion Sort'
            for item in insert(i+1, input_list[i+1], res_insert):
                print item,
            #break
            exit()

    res_merge = []
    for i in range(num):
        res_merge.append([input_list[i]])

    while len(res_merge) != 1:
        res_merge = merge(res_merge)
        res_merge_list = make_list(res_merge)
        if res_merge_list == some_list:
            print 'Merge Sort'
            res_merge = merge(res_merge)
            res_merge_list = make_list(res_merge)
            for item in res_merge_list:
                print item,
            exit()

