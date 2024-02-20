def celebrationParty(points):
    L = len(points)-1
    R = 0
    i = 0
    while i <= L:
        # P = points[i]
        r = points[i]+1
        R += 1
        i += 1
        while i <= L and points[i] <= r:
            i += 1
    return R
if __name__ == '__main__':
    points = map(float, input().split())
    print(celebrationParty(list(points)))