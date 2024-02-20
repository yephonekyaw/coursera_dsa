# python3
import sys

def compute_prefix(pt):
    longest_boarder = 0
    boarder_list = [0] * len(pt)
    for i in range(1, len(pt)):
        while longest_boarder > 0 and pt[i] != pt[longest_boarder]:
            longest_boarder = boarder_list[longest_boarder-1]
        if pt[longest_boarder] == pt[i]:
            longest_boarder += 1
        else:
            longest_boarder = 0
        boarder_list[i] = longest_boarder
    return boarder_list

def find_pattern(pattern, text):
    pt = pattern + '$' + text
    boarder_list = compute_prefix(pt)
    result = []
    for i in range(len(pattern)+1, len(pt)):
        if boarder_list[i] == len(pattern):
            result.append(i - (2*len(pattern)))
    return result

if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
