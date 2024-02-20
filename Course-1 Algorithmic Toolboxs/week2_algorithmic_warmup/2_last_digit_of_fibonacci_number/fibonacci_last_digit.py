# Uses python3
import sys
def get_fibonacci_last_digit_naive(n):
    p, c = 0, 1
    for i in range(n-1):
        p, c = c, (p+c) % 10
    return c
if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
