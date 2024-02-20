# python3
import sys

# only to compute sorted first col of bwt
def count_sort(bwt):
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
    
    first_col = [0] * len(bwt)
    first_col[0] = '$'
    for char in bwt:
        if char != '$':
            index = ord(char) - ord('A') + 1
            new_index = pos[index]
            first_col[new_index] = char
            pos[index] += 1
    return first_col

def precompute_occ_counts_before(bwt, starts):
    occ_counts_before = {}
    last_end = {}
    last_val = {}
    for key in starts.keys():
        last_end[key] = 0
        last_val[key] = 0
        occ_counts_before[key] = [0] * (len(bwt) + 1)

    for i in range(len(bwt)):
        char = bwt[i]
        end = last_end[char]
        val = last_val[char]
        if end != 0:
            for index in range(end+1, i+1):
                occ_counts_before[char][index] = val
        occ_counts_before[char][i+1] = val + 1
        last_val[char] = val + 1
        last_end[char] = i + 1
    # last_end is used to assign last_val if occ_counts_before[char][i] == 0
    # ans i > last_end
    # because all the value of occurence of char beyond last_end is last_val
    return occ_counts_before, last_end, last_val

def PreprocessBWT(bwt):
    first_col = count_sort(bwt)
    starts = {}
    for no in range(len(first_col)):
        if starts.get(first_col[no]) == None:
            starts[first_col[no]] = no
    
    occ_counts_before, last_end, last_val = precompute_occ_counts_before(bwt, starts)
    return starts, occ_counts_before, last_end, last_val

def CountOccurrences(pattern, bwt, starts, occ_counts_before, last_end, last_val):
    top = 0
    bottom = len(bwt) - 1
    length = len(pattern) - 1
    while top <= bottom:
        if length >= 0:
            char = pattern[length]
            length -= 1
            # check if char is present in text
            if starts.get(char) != None:
                tem_top = top 
                tem_bottom = bottom + 1

                top = starts[char] + occ_counts_before[char][top]
                bottom = starts[char] + occ_counts_before[char][bottom + 1] - 1

                # if top and bottom + 1 values are larger than last_enc[char]
                # then existing value in occ_counts_before[char][top] or
                # occ_counts_before[char][bottom + 1] is just zero
                # but acutal value is last_val[char]
                if tem_top > last_end[char]:
                    top += last_val[char]
                if tem_bottom > last_end[char]:
                    bottom += last_val[char]
            else:
                break
        else:
            return bottom - top + 1
    return 0

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    starts, occ_counts_before, last_end, last_val = PreprocessBWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
      occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before, last_end, last_val))
    print(' '.join(map(str, occurrence_counts)))