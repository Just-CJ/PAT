__author__ = 'Just_CJ'

import re

if __name__ == '__main__':
    type, need = map(int, re.split(r'\s+(?!$)', raw_input()))
    stock = map(float, re.split(r'\s+(?!$)', raw_input()))
    price_all = map(float, re.split(r'\s+(?!$)', raw_input()))
    dict = {}
    for i in range(min(len(stock), len(price_all))):
        dict[i] = (stock[i], price_all[i])

    list = sorted(dict.iteritems(), key = lambda x:float(x[1][1])/x[1][0], reverse=True)
    profit = 0
    sold = 0
    for i in range(len(list)):
        if sold+list[i][1][0] < need:
            sold += list[i][1][0]
            profit += list[i][1][1]
        else:
            profit += float(need-sold)/list[i][1][0]*list[i][1][1]
            break

    print '%.2f' % profit


