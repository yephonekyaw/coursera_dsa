#Uses python3

import sys
def number_of_components(adj, visited):
    result = 0
    for vertix in range(len(visited)):
        if not visited[vertix]:
            explore(adj, vertix, visited, result)
            result += 1
    return result

def explore(adj, v, visited, result):
    visited[v] = True
    for vertix in adj[v]:
        if not visited[vertix]:
            explore(adj, vertix, visited, result)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    visited = [False for _ in range(n)]
    print(number_of_components(adj, visited))