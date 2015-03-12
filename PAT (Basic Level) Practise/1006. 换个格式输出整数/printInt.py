__author__ = 'Just_CJ'

if __name__ == '__main__':
    num = int(raw_input())
    num_B = num/100
    num_S = (num%100)/10
    num_D = num%10

    str_D = ''
    for i in range(num_D):
        str_D += str(i+1)

    print num_B*'B'+num_S*'S'+str_D

