import sys
from math import ceil
def get_majority_element(a, l, r):
    if l == r:
        return -1
    if l + 1 == r:
        return 0 if a[l]==a[r] else -1 
    if countSort(a):
        return 1
    else:
        return -1

def countSort(a):
    a_count = dict()
    for i in a:
        a_count[i] = a_count.get(i, 0)+1
    for i in a_count:
        if a_count[i] > (n//2):
            return True
    return False  

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)