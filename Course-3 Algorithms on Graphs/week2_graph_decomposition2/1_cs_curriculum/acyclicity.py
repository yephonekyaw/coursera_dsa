#Uses python3
import sys

def acyclic(adj):
    visited = [False] * len(adj)
    for vertex in range(len(visited)):
        if not visited[vertex]:
            path = vertex
            if explore(adj, vertex, path, visited):
                return 1
    return 0

def explore(adj, v, path, visited):
    visited[v] = True
    for vertex in adj[v]:
        if not visited[vertex]:
            if explore(adj, vertex, path, visited):
                return True
        if visited[vertex] and path == vertex:
            return True
    return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))