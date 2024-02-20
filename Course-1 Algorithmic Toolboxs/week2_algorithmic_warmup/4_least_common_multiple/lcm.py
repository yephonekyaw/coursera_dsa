# Uses python3
import sys
import time
def lcm_best(a, b):
    if b == 0:
        return a
    return lcm_best(b, a%b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print((a*b)//lcm_best(a, b))

