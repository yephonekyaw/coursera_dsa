#Uses python3

import sys

def lcs2(a, b):
    d = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            insertion = d[i][j-1]
            delection = d[i-1][j]
            match = d[i-1][j-1]+1
            if a[i-1]==b[j-1]:
                d[i][j] = max(insertion, delection, match)
            else:
                d[i][j] = max(insertion,delection)

    return d[len(a)][len(b)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
