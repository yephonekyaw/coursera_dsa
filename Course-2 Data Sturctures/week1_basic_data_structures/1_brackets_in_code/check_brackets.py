# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_brackets_stack_pos = []

    if len(text)==1:
        return 1

    for i, next in enumerate(text):
        bkt = Bracket(next, str(i+1))
        if next in "([{":
            opening_brackets_stack.append(next)
            opening_brackets_stack_pos.append(i+1)
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return bkt[1]
            
            left = opening_brackets_stack.pop()
            right = bkt[0]
            if are_matching(left, right):
                opening_brackets_stack_pos.pop()
                continue
            else:
                return bkt[1]
    if len(opening_brackets_stack_pos) > 0:
        return opening_brackets_stack_pos[0]
    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
