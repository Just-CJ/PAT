__author__ = 'Just_CJ'

import time, re, datetime

if __name__ == '__main__':
    C1, C2 = map(int, re.split(r'\s+(?!$)', raw_input()))
    during = round(float(C2-C1)/100)
    sec = during%60
    min = (during-sec)/60%60
    hour = ((during-sec)/60-min)/60
    print "%02d:%02d:%02d" % (hour, min, sec)