# Uses python3
import sys
import math
def binary_search(a, x, l, r):
    if r<l:
        return -1

    mid = math.floor((l+r)/2)
    if a[mid]==x:
        return mid
    elif a[mid]<x:
        return binary_search(a, x, mid+1, r)
    else:
        return binary_search(a, x, l, mid-1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x, 0, len(a)-1), end = ' ')