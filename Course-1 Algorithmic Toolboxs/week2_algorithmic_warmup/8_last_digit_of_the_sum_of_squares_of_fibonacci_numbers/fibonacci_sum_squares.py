# Uses python3
from sys import stdin

def fibonacci_sum_squares_best(n):
    p, c = 0, 1
    if n==0 or n==1:
        return n
    else:
        n = n%60
        if n==0:
            return n
        for i in range(2,n+1):
            p, c = c, (p+c)%60
        
        return c

if __name__ == '__main__':
    n = int(input())
    final = fibonacci_sum_squares_best(n)*fibonacci_sum_squares_best(n+1)
    print(final % 10)
