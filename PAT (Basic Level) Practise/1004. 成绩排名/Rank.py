__author__ = 'Just_CJ'

if __name__ == '__main__':
    num = int(raw_input())
    dict = {}

    for i in range(num):
        str = raw_input()
        info = str.split(' ')
        dict[(info[0], info[1])] = int(info[2])

    rank_first = max(dict.items(), key=lambda x:x[1])
    rank_last = min(dict.items(), key=lambda x:x[1])

    print rank_first[0][0]+' '+rank_first[0][1]
    print rank_last[0][0]+' '+rank_last[0][1]
