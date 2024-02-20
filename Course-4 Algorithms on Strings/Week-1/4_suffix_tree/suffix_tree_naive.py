# python3
# time complexity = O(n^2)
# space complexity = O(|Text|)
import sys
from collections import deque

class Node():
  def __init__(self, lab):
    self.lab = lab
    self.out = {}
    # you can apply DFS even without visited
    self.visited = False

def bulid_tree(root, text):
  for i in range(len(text)):
    cur = root
    j = i
    while j < len(text):
      # there is a node start with the character text[j]
      if text[j] in cur.out:
          child = cur.out[text[j]]
          lab = child.lab

          # finding the first mismatch
          k = j+1
          while k-j < len(lab) and text[k] == lab[k-j]:
            k += 1
          if k-j == len(lab):
            cur = child
            j = k
          else:
            cExist, cNew = lab[k-j], text[k]
            mid = Node(lab[:k-j])
            mid.out[cNew] = Node(text[k:])
            mid.out[cExist] = child
            child.lab = lab[k-j:]
            cur.out[text[j]] = mid
      else:
        cur.out[text[j]] = Node(text[j:])
        break

# def dfs_recursive(root, result):
#   root.visited = True
#   objs = root.out.keys()
#   for key in objs:
#     cur = root.out[key]
#     if not cur.visited:
#       dfs_recursive(cur, result)
#   if root.lab != None:
#     result.append(root.lab)

def dfs_while(root, result):
  nodes = deque()
  nodes.append(root)
  while nodes:
    node = nodes.pop()
    keys = node.out.keys()
    if not node.visited and node.lab != None:
      result.append(node.lab)
      node.visited = True
    for key in keys:
      cur = node.out[key]
      if not cur.visited:
        nodes.append(cur)


def suffix_tree(text):
  result = []
  root = Node(None)
  bulid_tree(root, text)
  dfs_while(root, result)
  return result

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = suffix_tree(text)
  print("\n".join(result))
