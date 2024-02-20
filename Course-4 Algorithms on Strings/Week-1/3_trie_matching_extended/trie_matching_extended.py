# python3
import sys

class Node:
	def __init__ (self):
		# only four characters : A, C, G, T
		self.next = [None] * 26
		self.isLeaf = False

def createTries(root, patterns):
	for pattern in patterns:
		currentNode = root
		for char in pattern:
			index = ord(char)-ord('A')

			if currentNode.next[index] == None:
				currentNode.next[index] = Node()

			# change root to new character or edge
			currentNode = currentNode.next[index]
		# set to leaf condition
		currentNode.isLeaf = True

def search(result, root, text):
	for i in range(len(text)):
		currentNode = root
		j = i
		while(j < len(text)):
			index = ord(text[j])-ord('A')
			if currentNode.next[index] != None:
				currentNode = currentNode.next[index]
				j += 1
				# check isLeaf to add an occurent point
				if currentNode.isLeaf:
					if i not in result:
						result.append(i)
					break
			else:
				break

def solve (text, n, patterns):
	result = []
	# create the root of trie
	root = Node()
	# create tries of patterns
	createTries(root, patterns)
	# search each occurences
	search(result, root, text)
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
