__author__ = 'Just_CJ'

if __name__ == '__main__':
    argv = raw_input()
    num = int(argv.split(' ')[0])
    shift = int(argv.split(' ')[1])
    line = raw_input()
    arr = []
    for i in range(num):
        arr.append(line.split(' ')[i])

    for i in range(shift):
        tmp = arr[num-1]
        for j in range(num-1, 0, -1):
            arr[j] = arr[j-1]
        arr[0] = tmp

    for i in arr:
        print i,
