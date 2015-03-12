__author__ = 'Just_CJ'

if __name__ == '__main__':
    num = int(raw_input())
    list = []
    line = raw_input()
    for i in range(num):
        list.append(int(line.split(' ')[i]))

    left = list[:]

    for i in list:
        n = i
        while n != 1:
            if n%2 == 0:
                n /= 2
            else:
                n = (3*n+1)/2

            if n in left:
                left.remove(n)

    left.sort(reverse=True)

    for i in left:
        print i,
