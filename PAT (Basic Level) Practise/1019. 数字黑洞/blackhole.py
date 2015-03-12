__author__ = 'Just_CJ'

if __name__ == '__main__':
    num = raw_input()
    if len(num) < 4:
        num = (4-len(num))*'0'+num
    while True:
        A = ''.join(sorted(num, reverse=True))
        B = ''.join(sorted(num, reverse=False))
        num = str(int(A)-int(B))
        if len(num) < 4:
            num = (4-len(num))*'0'+num
        print A, '-', B, '=', num
        if num == '0000' or num == '6174':
            break
