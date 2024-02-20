# python3
import sys

def BWT(text):
    tem_text = text * 2
    rotations = [tem_text[i:i+len(text)] for i in range(len(text))]
    rotations = sorted(rotations)
    return ''.join(map(lambda x : x[-1], rotations))

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))