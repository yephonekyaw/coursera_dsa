# python3
# # python3
import sys
from collections import deque

class Node():
    def __init__(self, parent, depth, start, end):
        self.children = [-1] * 27
        self.parent = parent
        self.depth = depth
        self.start = start
        self.end = end 

def create_new_node(text, node, suffix):
    depth = len(text) - suffix
    start = suffix + node.depth
    end = len(text) - 1
    new_node = Node(node, depth, start, end)
    index = -1
    if text[start] == '$':
        index = 0
    else:
        index = ord(text[start]) - ord('A') + 1
    node.children[index] = new_node
    return new_node

def break_edge(text, node, start, offset):
    start_char = text[start]
    mid_char = text[start + offset]
    mid_depth = node.depth + offset
    mid_start = start
    mid_end = start + offset - 1
    mid_node = Node(node, mid_depth, mid_start, mid_end)
    
    # change child, parent, node_no
    if start_char == '$':
        start_char = 0
    else:
        start_char = ord(start_char) - ord('A') + 1
    child = node.children[start_char]
    child.parent = mid_node
    child.start += offset

    if mid_char == '$':
        mid_char = 0
    else:
        mid_char = ord(mid_char) - ord('A') + 1
    mid_node.children[mid_char] = child
    node.children[start_char] = mid_node
    return mid_node

def suffix_array_to_suffix_tree(sa, lcp, text):
    tree = {}
    node_no = 0
    root = Node(None, 0, -1, -1)
    pre_lcp = 0
    cur_node = root
    for i in range(len(text)):
        suffix = sa[i]
        while cur_node.depth > pre_lcp:
            cur_node = cur_node.parent
        
        if cur_node.depth == pre_lcp:
            # create new leaf node
            cur_node = create_new_node(text, cur_node, suffix)
        else:            
            # break the existing node and
            # create new internal node and
            # modify old leaf node
            edge_start = sa[i - 1] + cur_node.depth
            offest = pre_lcp - cur_node.depth
            mid_node = break_edge(text, cur_node, edge_start, offest)

            # create new leaf
            node_no += 1
            cur_node = create_new_node(text, mid_node, suffix)

        if i < (len(text) - 1):
            pre_lcp = lcp[i]
    
    return root

def pre_order(root):
    nodes = [node for node in root.children[::-1] if node != -1]
    
    while nodes:
        node = nodes.pop()
        print(node.start, node.end + 1)
        for child in node.children[::-1]:
            if child != -1:
                nodes.append(child)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    root = suffix_array_to_suffix_tree(sa, lcp, text)
    print(text)
    pre_order(root)