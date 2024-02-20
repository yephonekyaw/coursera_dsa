# python3
import sys

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

def find_occurrences(text, patterns):
    suffix_array = build_suffix_array(text)
    occs = set()
    
    for pattern in patterns:
        # do binary search twice to get start, end indices
        minIndex = 0
        maxIndex = len(text)
        while minIndex < maxIndex:
            midIndex = (minIndex + maxIndex)//2
            if pattern > text[suffix_array[midIndex]:]:
                minIndex = midIndex + 1
            else:
                maxIndex = midIndex
        start = minIndex

        minIndex = 0
        maxIndex = len(text)
        while minIndex < maxIndex:
            midIndex = (minIndex + maxIndex)//2
            mid_suffix = text[suffix_array[midIndex]:]
            if mid_suffix.startswith(pattern):
                minIndex = midIndex + 1
            elif pattern < mid_suffix:
                maxIndex = midIndex
            else:
                minIndex = midIndex + 1    
        end = maxIndex
        
        if start <= end:
            tem_occ = set(suffix_array[start:end])
            occs = occs.union(tem_occ)
    return occs

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    text += '$'
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))