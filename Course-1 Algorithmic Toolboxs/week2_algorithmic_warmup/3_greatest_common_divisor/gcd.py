# Uses python3
import sys
def gcd_best(a, b):
    if b == 0:
        return a
    return gcd_best(b, a%b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_best(a, b))
