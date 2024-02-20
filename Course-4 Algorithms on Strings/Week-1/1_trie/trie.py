#Uses python3
import sys
def build_trie(patterns):
    tree = dict()
    nodeNo = 1
    for pattern in patterns:
        currentNode = 0
        for char in pattern:            
            if currentNode in tree.keys() and char in tree[currentNode].keys():
                currentNode = tree[currentNode][char]
            else:
                if currentNode in tree.keys():
                    tree[currentNode].update({char:nodeNo})
                else:
                    tree[currentNode] = {char:nodeNo}
                currentNode = nodeNo
                nodeNo += 1
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
