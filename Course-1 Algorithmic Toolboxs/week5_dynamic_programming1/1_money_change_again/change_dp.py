# Uses python3
import sys

def get_change(m):
    coins = [1, 3, 4]
    minNumCoins = [0 for i in range(m+1)]
    for i in range(1, m+1):
        minNumCoins[i] = 10001
        for j in coins:
            if i >= j:
                numCoins = minNumCoins[i-j]+1
                if numCoins < minNumCoins[i]:
                    minNumCoins[i] = numCoins

    return minNumCoins[m]
    
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
