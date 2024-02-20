# Uses python3
import sys
def pisanoPeriod(m):
    p, c = 0, 1
    for i in range(0, m * m):
        p, c = c, (p+c)%m
         
        # A Pisano Period starts with 01
        if (p == 0 and c == 1):
            return i + 1

def get_fibonacci_huge_best(n, m):
    # calculate pisano period length
    p_len = pisanoPeriod(m)
    print(p_len)
    n = n % p_len
    p, c = 0, 1
    if n == 0 or n == 1:
        return n
    for i in range(n-1):
        p, c = c, p+c
    return (c % m)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_best(n, m))