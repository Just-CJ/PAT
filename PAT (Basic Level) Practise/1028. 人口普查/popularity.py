__author__ = 'Just_CJ'

import re
import datetime
if __name__ == '__main__':
    num = int(raw_input())
    today = datetime.date(2014, 9, 6)
    min_p = ['', 200*266]
    max_p = ['', -1]
    eff_num = 0

    for i in range(num):
        name, birth = re.split(r'\s+(?!$)', raw_input())
        birth = birth.split('/')
        birth = datetime.date(int(birth[0]), int(birth[1]), int(birth[2]))

        if birth < datetime.date(1814, 9, 6) or birth > today:
            continue
        else:
            eff_num += 1
            years = today - birth
            if years.days > max_p[1]:
                max_p[0] = name
                max_p[1] = years.days
            if years.days < min_p[1]:
                min_p[0] = name
                min_p[1] = years.days
    if eff_num:
        print eff_num, max_p[0], min_p[0]
    else:
        print eff_num