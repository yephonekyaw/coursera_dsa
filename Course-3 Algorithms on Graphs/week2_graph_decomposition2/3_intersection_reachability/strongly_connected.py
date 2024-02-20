#Uses python3

import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj, reversed_adj):
    result = 0
    
    # run depth first search on reversed directed graph
    post_order = reversed_dfs(reversed_adj)
    
    # calculate SCCs
    visited = [False] * len(adj)
    for vertex in post_order:
        if not visited[vertex]:
            explore(adj, vertex, visited)
            result += 1
    return result

def reversed_dfs(reversed_adj):
    visited = [False] * len(reversed_adj)
    post_order =[]
    for vertex in range(len(reversed_adj)):
        if not visited[vertex]:
            reversed_explore(reversed_adj, vertex, visited, post_order)
    return post_order[::-1]

def reversed_explore(reversed_adj, v, visited, post_order):
    visited[v] = True
    for vertex in reversed_adj[v]:
        if not visited[vertex]:
            reversed_explore(reversed_adj, vertex, visited, post_order)
    post_order.append(v)

def explore(adj, v, visited):
    visited[v] = True
    for vertex in adj[v]:
        if not visited[vertex]:
            explore(adj, vertex, visited)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    reversed_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        reversed_adj[b-1].append(a-1)
    print(number_of_strongly_connected_components(adj, reversed_adj))
