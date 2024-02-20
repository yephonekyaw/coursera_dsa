import sys

def build_suffix_array(text):
    result = []
    tem_text = text * 2
    rotations = {tem_text[i:i+len(text)] : i for i in range(len(text))}
    suffixs = sorted(rotations.keys())
    for key in suffixs:
        result.append(rotations[key])
    return result

def invert_suffix_array(suffix_array):
    pos = [0] * len(suffix_array)
    for i in range(len(suffix_array)):
        pos[suffix_array[i]] = i
    return pos

def lcp_of_two_suffixes(text, i, j , lcp):
    lcp = max(0, lcp)
    while i + lcp < len(text) and j + lcp < len(text):
        if text[i + lcp] == text[j + lcp]:
            lcp += 1
        else:
            break
    return lcp

def build_lcp_array(text, suffix_array):
    lcp_array = [0] * (len(suffix_array) - 1)
    posInOrder = invert_suffix_array(suffix_array)
    lcp = 0
    suffix = suffix_array[0]
    for i in range(len(text)):
        orderIndex = posInOrder[suffix]
        if orderIndex == len(text) - 1:
            lcp = 0
            suffix = (suffix + 1) % len(text)
            continue
        next_suffix = suffix_array[orderIndex + 1]
        lcp = lcp_of_two_suffixes(text, suffix, next_suffix, lcp - 1)
        lcp_array[orderIndex] = lcp
        suffix = (suffix + 1) % len(text)
    return lcp_array

def build_lcp_LR_array(lcp_LR, lcp_array, l, r):
    if (l + 1) == r:
        lcp_LR[l][r] = lcp_array[l]
        return
    
    m = (l + r)//2
    build_lcp_LR_array(lcp_LR, lcp_array, l, m)
    build_lcp_LR_array(lcp_LR, lcp_array, m, r)

    if l != 0 or r != len(lcp_array):
        lcp_LR[l][r] = min(lcp_LR[l][m], lcp_LR[m][r])
        

def compute_lcp_of_pattern_and_mid(text, pattern, pos, lcp):

    while (lcp + pos) < len(text) and lcp < len(pattern):
        if pattern[lcp] == text[lcp + pos]:
            lcp += 1
        else:
            break
    return lcp

def find_occurrences(text, patterns, suffix_array, lcp_LR):

    occs = set()
    for pattern in patterns:
        # find a range between left and right
        l1 = compute_lcp_of_pattern_and_mid(text, pattern, suffix_array[0], 0)
        r1 = compute_lcp_of_pattern_and_mid(text, pattern, suffix_array[len(text)-1], 0)
        l2, r2 = l1, r1
        p = len(pattern)
        minIndex = 0
        maxIndex = len(text) - 1
        while maxIndex - minIndex > 1:
            midIndex = (minIndex + maxIndex)//2
            if l1 >= r1:
                if lcp_LR[minIndex][midIndex] >= l1:
                    m = compute_lcp_of_pattern_and_mid(text, pattern, suffix_array[midIndex], l1)
                else:
                    m = lcp_LR[minIndex][midIndex]
            else:
                if lcp_LR[midIndex][maxIndex] >= r1:
                    m = compute_lcp_of_pattern_and_mid(text, pattern, suffix_array[midIndex], r1)
                else:
                    m = lcp_LR[midIndex][maxIndex]
            if m == p or pattern[m] <= text[suffix_array[midIndex] + m]:
                maxIndex = midIndex
                r1 = m
            else:
                minIndex = midIndex
                l1 = m
        L_w = maxIndex

        minIndex = 0
        maxIndex = len(text) - 1
        while maxIndex - minIndex > 1:
            midIndex = (minIndex + maxIndex)//2
            if l2 >= r2:
                if lcp_LR[minIndex][midIndex] >= l2:
                    m = compute_lcp_of_pattern_and_mid(text, pattern, suffix_array[midIndex], l2)
                else:
                    m = lcp_LR[minIndex][midIndex]
            else:
                if lcp_LR[midIndex][maxIndex] >= r2:
                    m = compute_lcp_of_pattern_and_mid(text, pattern, suffix_array[midIndex], r2)
                else:
                    m = lcp_LR[midIndex][maxIndex]
            if m == p or pattern[m] == text[suffix_array[midIndex] + m]:
                minIndex = midIndex
                l2 = m
            elif pattern[m] < text[suffix_array[midIndex] + m]:
                maxIndex = midIndex
                r2 = m
            else:
                minIndex = midIndex
                l2 = m
        R_w = maxIndex
        
        if L_w < R_w:
            pos = suffix_array[R_w]
            tem_occ = None
            if pattern == text[pos:(pos + len(pattern))]:
                tem_occ = set(suffix_array[L_w:R_w + 1])
            else:
                tem_occ = set(suffix_array[L_w:R_w])
            occs = occs.union(tem_occ)
        elif L_w == R_w:
            pos = suffix_array[L_w]
            if pattern == text[pos:(pos + len(pattern))]:
                occs.add(suffix_array[L_w])
            
    return occs

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    patterns = sys.stdin.readline().strip().split()
    suffix_array = build_suffix_array(text)
    lcp_array = build_lcp_array(text, suffix_array)
    
    lcp_LR = [{} for i in range(len(text) - 1)]
    build_lcp_LR_array(lcp_LR, lcp_array, 0, len(text) - 1)

    occs = find_occurrences(text, patterns, suffix_array, lcp_LR)
    print(" ".join(map(str, occs)))