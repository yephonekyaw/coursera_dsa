# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    def inOrder_recursive(key):
      if key == -1:
        return
      inOrder_recursive(self.left[key])
      self.result.append(self.key[key])
      inOrder_recursive(self.right[key])
    inOrder_recursive(0)
    return self.result

  def preOrder(self):
    self.result = []
    def preOrder_recursive(key):
      if key == -1:
        return 
      self.result.append(self.key[key])
      preOrder_recursive(self.left[key])
      preOrder_recursive(self.right[key])
    preOrder_recursive(0)
    return self.result

  def postOrder(self):
    self.result = []
    def postOrder_recursive(key):
      if key == -1:
        return 
      postOrder_recursive(self.left[key])
      postOrder_recursive(self.right[key])
      self.result.append(self.key[key])
    postOrder_recursive(0)            
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
