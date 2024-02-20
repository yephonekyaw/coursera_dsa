#Uses python3

import sys

def dfs(adj, used, order, x):
    used[x] = 1
    for vertex in adj[x]:
        if used[vertex] == 0:
            dfs(adj, used, order, vertex)
    order.append(x)

def toposort(adj):
    used = [0] * len(adj)
    order = []
    for vertex in range(len(adj)):
        if used[vertex] == 0:
            dfs(adj, used, order, vertex)
    return order[::-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

