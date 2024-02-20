# python3
import sys

def build_suffix_array(text):
    result = []
    tem_text = text * 2
    rotations = {tem_text[i:i+len(text)] : i for i in range(len(text))}
    suffixs = sorted(rotations.keys())
    for key in suffixs:
        result.append(rotations[key])
    return result 


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))