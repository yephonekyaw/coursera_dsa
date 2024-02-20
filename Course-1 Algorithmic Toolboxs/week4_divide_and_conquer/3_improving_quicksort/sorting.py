# Uses python3
import sys
import random

def partition3(a, l, r):
    key = a[l]
    i, j = l, l
    end = r
    while j <= end:
        if a[j] < key:
            a[j], a[i] = a[i], a[j]
            i += 1
            j += 1
        elif a[j] > key:
            a[j], a[end] = a[end], a[j]
            end -= 1
        else:
            j += 1
    return i, j-1

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2+1, r)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n-1)
    for x in a:
        print(x, end=' ')