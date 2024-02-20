def from_text_to_BWT(text):
    tem_text = text * 2
    rotations = [tem_text[i:i+len(text)] for i in range(len(text))]
    rotations = sorted(rotations)
    return ''.join(map(lambda x : x[-1], rotations))

def from_BWT_to_text(bwt_text):
    _count = {}
    original_t = {}
    for no, char in enumerate(bwt_text):
        if _count.get(char) != None:
            present_count = _count.get(char)
            present_count += 1
        else:
            present_count = 1
        _count[char] = present_count
        char += str(present_count)
        original_t[char] = no
    
    first_col = sorted(original_t.keys(), key=lambda x: x[0])
    last_col = list(original_t.keys())

    for no, char in enumerate(first_col):
        original_t[char] = no #original_t.values are position of last col to first col
    
    text = '$'
    index = 0
    while last_col[index][0] != '$':
        cur_char = last_col[index]
        index = original_t[cur_char]
        text += cur_char[0]

    return text[::-1]

if __name__ == '__main__':
    text = input()
    bwt_text = None
    if text[-1] != '$':
        text += '$'
    bwt_text = from_text_to_BWT(text)
    print(from_BWT_to_text(bwt_text))