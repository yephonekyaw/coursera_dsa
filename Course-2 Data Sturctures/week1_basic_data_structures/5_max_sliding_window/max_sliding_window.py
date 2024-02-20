# I made a mistake by using for loop instead of while loop
# in clearing all elements <= new element 

from collections import deque
def max_sliding_window(sequence, m):
    maximums = []
    max_deque = deque()
    for i in range(len(sequence)):
        # clear all element equal or smaller than new element
        new_element = sequence[i]
        while max_deque and new_element >= sequence[max_deque[-1]]:
            max_deque.pop()
        
        # append new element position to max_deque
        max_deque.append(i)

        # remove previous window's leftmost element
        if i >= m:
            remove_win_pos = i-m
            while max_deque and max_deque[0] <= remove_win_pos:
                max_deque.popleft()
            maximums.append(sequence[max_deque[0]])
        
        # append maximum for the very first window
        if i==m-1:
            maximums.append(sequence[max_deque[0]])
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))