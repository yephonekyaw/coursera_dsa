# Uses python3
import sys

def optimal_summands(n):
    summands = []
    k, l = n, 1
    while k>0:
        if (k <= 2*l):
            summands.append(k)
            k -= k
        else:
            summands.append(l)
            k -= l
        l+=1    
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
