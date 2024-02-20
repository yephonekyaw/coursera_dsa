# python3

import sys

class Rope:
	def __init__(self, s):
		self.s = s
	def result(self):
		return self.s
	def process(self, i, j, k):
		if k == 0:
			sub_str = self.s[i:j+1]
			self.s = self.s[0:i] + self.s[j+1:]
			self.s = sub_str + self.s
		else:
			sub_str = self.s[i:j+1]
			self.s = self.s[0:i] + self.s[j+1:]
			k = k-1
			self.s = self.s[0:k+1] + sub_str + self.s[k+1:]

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
