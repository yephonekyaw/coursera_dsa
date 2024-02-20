# python3
from math import floor

def parent(pt):
    return floor((pt-1)/2) 

def left_child(pt):
    return (2*pt)+1

def right_child(pt):
    return (2*pt)+2

def sift_down(pt, swaps):
    size = len(data)
    minIndex = pt
    l = left_child(pt)
    if l<size and data[l]<data[minIndex]:
        minIndex = l
    r = right_child(pt)
    if r<size and data[r]<data[minIndex]:
        minIndex = r
    if pt!=minIndex:
        data[pt], data[minIndex] = data[minIndex], data[pt]
        swaps.append((pt, minIndex))
        sift_down(minIndex, swaps)

def build_heap(data):
    swaps = []
    parents = floor((len(data)-1)/2)
    for i in range(parents, -1, -1):
        sift_down(i, swaps)
    return swaps

if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
