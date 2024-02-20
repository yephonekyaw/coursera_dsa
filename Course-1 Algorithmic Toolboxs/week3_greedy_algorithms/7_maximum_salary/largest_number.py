#Uses python3

import sys
def IsGreaterOrEqual(digit, maxDigit):
    d1 = str(digit)+str(maxDigit)
    d2 = str(maxDigit)+str(digit)
    return d1>=d2

def largest_number(a):
    res = ''
    while a != []:
        maxDigit = 0
        for digit in a:
            if IsGreaterOrEqual(digit, maxDigit):
                maxDigit = digit
        res += str(maxDigit)
        a.remove(maxDigit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    a = data[1:]
    print(largest_number(a))
    