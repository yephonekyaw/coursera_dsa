# python3
import sys
from collections import deque

class Node():
    def __init__(self, parent, depth, start, end):
        self.children = {}
        self.parent = parent
        self.depth = depth
        self.start = start
        self.end = end 

def create_new_node(text, node, suffix):
    depth = len(text) - suffix
    start = suffix + node.depth
    end = len(text) - 1
    new_node = Node(node, depth, start, end)
    node.children[text[start]] = new_node
    return new_node

def break_edge(text, node, start, offset):
    start_char = text[start]
    mid_char = text[start + offset]
    mid_depth = node.depth + offset
    mid_start = start
    mid_end = start + offset - 1
    mid_node = Node(node, mid_depth, mid_start, mid_end)
    
    # change child, parent, node_no
    child = node.children[start_char]
    child.parent = mid_node
    child.start += offset

    mid_node.children[mid_char] = child
    node.children[start_char] = mid_node
    return mid_node

def pre_order(root):
    tree = []
    vals = list(root.children.values())
    nodes = vals[::-1]
    
    while nodes:
        node = nodes.pop()
        tree.append('{} {}\n'.format(node.start, node.end + 1))
        if len(node.children) != 0:
            vals = list(node.children.values())
            for i in vals[::-1]:
                nodes.append(i)

    return tree

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

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    root = suffix_array_to_suffix_tree(sa, lcp, text)
    tree = pre_order(root)
    
    for edge in tree:
        print(edge)