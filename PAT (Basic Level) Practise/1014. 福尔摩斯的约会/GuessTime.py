__author__ = 'Just_CJ'
import re

if __name__ == '__main__':
    str1 = raw_input()
    str2 = raw_input()
    str3 = raw_input()
    str4 = raw_input()

    dict_Day = {'A':'MON', 'B':'TUE', 'C':'WED', 'D':'THU', 'E':'FRI', 'F':'SAT', 'G':'SUN'}
    dict_HH = {'0':'00', '1':'01', '2':'02', '3':'03', '4':'04', '5':'05', '6':'06',
               '7':'07', '8':'08', '9':'09', 'A':'10', 'B':'11', 'C':'12', 'D':'13',
               'E':'14', 'F':'15', 'G':'16', 'H':'17', 'I':'18', 'J':'19', 'K':'20',
               'L':'21', 'M':'22', 'N':'23'}
    findDay = False
    hour = ''
    for i in range(min(len(str1), len(str2))):
        if findDay:
            if str1[i]==str2[i] and ((ord(str1[i])>=ord('A') and ord(str1[i])<=ord('N')) or str1[i].isdigit()):
                hour = str1[i]
                break
        elif str1[i]==str2[i] and ord(str1[i])>=ord('A') and ord(str1[i])<=ord('G'):
            print dict_Day[str1[i]],
            findDay = True

    for i in range(min(len(str3), len(str4))):
        if str3[i]==str4[i] and str3[i].isalpha():
            min = str(i)
            break
    if len(min) == 1:
        min = '0'+min
    print dict_HH[hour]+':'+str(min)