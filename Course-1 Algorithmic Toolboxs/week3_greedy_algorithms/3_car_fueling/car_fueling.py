# python3
import sys


def compute_min_refills(distance, tank, stops):
    numR, curR = 0, 0
    stops.insert(0, 0)
    stops.append(distance)
    while curR < len(stops) - 1:
        lastR = curR
        while curR < len(stops)-1 and stops[curR+1]-stops[lastR] <= tank:
            curR += 1
        if curR == lastR:
            return -1
        if curR < len(stops) - 1:
            numR += 1
    return numR

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
