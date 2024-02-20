# Uses python3
import sys

def get_number_of_inversions(a, count):
    if len(a) == 1:
        return a
    else:
        mid = len(a)//2
        b = get_number_of_inversions(a[:mid], count)
        c = get_number_of_inversions(a[mid:], count)
        cur_s = merge(b, c, count)
    
    return cur_s

def merge(b, c, count):
    d = []
    i = 0
    j = 0
    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            d.append(b[i])
            i = i + 1
        else:
            d.append(c[j])
            j = j + 1
            count[0] += len(b)-i
    d += b[i:]
    d += c[j:]

    return d

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    count = [0]
    get_number_of_inversions(a, count)
    print(count[0])
