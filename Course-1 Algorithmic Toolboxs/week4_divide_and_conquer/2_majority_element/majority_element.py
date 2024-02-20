# Uses python3
import sys
from math import floor
def get_majority_element(a, l, r):
    if l == r:
        return -1
    if l + 1 == r:
        return 0 if a[l]==a[r] else -1 
    a_sort = mergeSort(a)
    for i in set(a_sort):
        if a_sort.count(i) > (n//2):
            return 1
    return -1

def mergeSort(a):
    n = len(a)-1
    if n+1 == 1:
        return a
    
    mid = floor(n/2)
    b = mergeSort(a[:mid+1])
    c = mergeSort(a[mid+1:])
    a_s = merge(b, c)
    return a_s
    
def merge(b,c):
    d = []
    i = 0
    j = 0
    while i < len(b) and j < len(c):
        if b[i] < c[j]:
            d.append(b[i])
            i = i + 1
        else:
            d.append(c[j])
            j = j + 1
    d += b[i:]
    d += c[j:]

    return d

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)