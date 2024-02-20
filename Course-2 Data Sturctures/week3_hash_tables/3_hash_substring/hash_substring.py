# python3
import random
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def _hash_fun(s, _prime, _multiplier):
    ans = 0
    for c in reversed(s):
        ans = ans*_multiplier + ord(c)
        ans = ((ans % _prime) + _prime) % _prime
    return ans

def pre_compute_hash(text, pattern_len, _prime, _multiplier):
    h = [0 for _ in range(len(text)-pattern_len+1)]
    start = len(text)-pattern_len
    end = len(text)
    s = text[start:end]
    h[start] = _hash_fun(s, _prime, _multiplier)
    y = 1
    for i in range(0, pattern_len):
        y = y*_multiplier
        y = ((y % _prime) + _prime) % _prime
    for i in range(start-1, -1, -1):
        h[i] = (_multiplier * h[i+1]) + ord(text[i]) - (y * ord(text[i+pattern_len]))
        h[i] = ((h[i] % _prime) + _prime) % _prime
    return h

def RabinKarp(pattern, text):
    _prime = 250000000007
    _multiplier = 263
    result = []
    pHash = _hash_fun(pattern, _prime, _multiplier)
    h = pre_compute_hash(text, len(pattern), _prime, _multiplier)
    for i in range(len(text)-len(pattern)+1):
        if pHash != h[i]:
            continue
        substring = i+len(pattern)
        if text[i:substring] == pattern:
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))