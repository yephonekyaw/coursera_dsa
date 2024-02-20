# python3
import sys

# part of building suffix_array
def first_cyclic_shift_sort(text):
    order = [0] * len(text)
    count = [0] * 27
    for i in text:
        if i == '$':
            count[0] = count[0] + 1
        else:
            index = ord(i) - ord('A') + 1
            count[index] = count[index] + 1

    for j in range(1, len(count)):
        count[j] = count[j] + count[j - 1]

    order[0] = len(text) - 1
    for k in range(len(text) - 1, -1, -1):
        if text[k] != '$':
            index = ord(text[k]) - ord('A') + 1
            count[index] = count[index] - 1
            order[count[index]] = k
    return order

def first_class_computing(order, text):
    old_class = [0] * len(text)
    for i in range(1, len(text)):
        if text[order[i]] != text[order[i - 1]]:
            old_class[order[i]] = old_class[order[i - 1]] + 1
        else:
            old_class[order[i]] = old_class[order[i - 1]]
    return old_class

def double_cyclic_shift_sort(length, text, order, old_class):
    count = [0] * len(text)
    new_order = [0] * len(text)
    for i in range(len(text)):
        count[old_class[i]] = count[old_class[i]] + 1
    
    for j in range(1, len(text)):
        count[j] = count[j] + count[j - 1]

    text_len = len(text)
    for k in range(len(text) - 1, -1, -1):
        start = (order[k] - length + text_len)%text_len
        cl = old_class[start]
        count[cl] = count[cl] - 1
        new_order[count[cl]] = start
    return new_order

def update_class(length, order, old_class):
    n = len(order)
    new_class = [0] * len(old_class)
    for i in range(1, len(order)):
        cur = order[i]
        prev = order[i - 1]
        midCur = (cur + length) % n
        midPrev = (prev + length) % n
        if old_class[cur] != old_class[prev] or old_class[midCur] != old_class[midPrev]:
            new_class[cur] = new_class[prev] + 1
        else:
            new_class[cur] = new_class[prev]
    return new_class
    
def build_suffix_array(text):
    order = first_cyclic_shift_sort(text)
    old_class = first_class_computing(order, text)
    length = 1
    while length < len(text):
        order = double_cyclic_shift_sort(length, text, order, old_class)
        old_class = update_class(length, order, old_class)
        length = 2 * length
    return order

# part of building lcp_array
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

# part of building lcp_LR array
def build_lcp_LR_array(lcp_LR, lcp_array, l, r):
    if (l + 1) == r:
        lcp_LR[l][r] = lcp_array[l]
        return
    
    m = (l + r)//2
    build_lcp_LR_array(lcp_LR, lcp_array, l, m)
    build_lcp_LR_array(lcp_LR, lcp_array, m, r)

    if l != 0 or r != len(lcp_array):
        lcp_LR[l][r] = min(lcp_LR[l][m], lcp_LR[m][r])

# part of searching algorithm
def compute_lcp_of_pattern_and_mid(text, pattern, pos, lcp):

    while (lcp + pos) < len(text) and lcp < len(pattern):
        if pattern[lcp] == text[lcp + pos]:
            lcp += 1
        else:
            break
    return lcp

def find_occurrences(text, patterns):
    suffix_array = build_suffix_array(text)

    lcp_array = build_lcp_array(text, suffix_array)
    
    lcp_LR = [{} for i in range(len(text) - 1)]
    build_lcp_LR_array(lcp_LR, lcp_array, 0, len(text) - 1)
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
    text += '$'
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))