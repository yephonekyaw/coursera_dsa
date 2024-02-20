# python3
import sys

def count_sort(bwt):
    last_to_first = [] #position of last col'char in first col
    count = [0] * 27 #for all english letters + $
    count[0] = 1 #for sign '$'
    for i in bwt:
        if i != '$':
            index = ord(i) - ord('A') + 1
            count[index] = count[index] + 1
    
    pos = [0] * 27
    pos[0] = 0
    for i in range(1, len(count)):
        pos[i] = pos[i-1] + count[i-1]
    
    res = [0] * len(bwt)
    res[0] = '$'
    for char in bwt:
        if char != '$':
            index = ord(char) - ord('A') + 1
            new_index = pos[index]
            res[new_index] = char
            last_to_first.append(new_index)
            pos[index] += 1
        else:
            last_to_first.append(0)
    
    return res, last_to_first

def InverseBWT(last_col):

    first_col, last_to_first = count_sort(last_col)
    text = ['$']
    index = 0
    while last_col[index] != '$':
        text.append(last_col[index])
        index = last_to_first[index]

    return ''.join(text[::-1])

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))