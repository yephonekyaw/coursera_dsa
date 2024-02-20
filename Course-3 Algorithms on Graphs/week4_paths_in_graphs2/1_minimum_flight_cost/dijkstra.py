#Uses python3

import sys
from sys import maxsize
import heapq


def distance(adj, cost, s, t):
    
    # declarations
    dist = [maxsize] * len(adj)
    prev = [None] * len(adj)
    vertex_heap = [] # min-heap

    # first assigning
    dist[s] = 0
    for i in range(len(adj)):
        value = (maxsize, i)
        if i == s:
            value = (0, i)
            heapq.heappush(vertex_heap, value)
        else:
            heapq.heappush(vertex_heap, value)

    # operations
    while vertex_heap:
        cur_len, cur_vertex = heapq.heappop(vertex_heap)
        for i in range(len(adj[cur_vertex])):
            vertex = adj[cur_vertex][i]
            if dist[vertex] > dist[cur_vertex] + cost[cur_vertex][i]:
                dist[vertex] = dist[cur_vertex] + cost[cur_vertex][i]
                prev[vertex] = cur_vertex
                
                # adding new element changed its distance
                value = (dist[vertex], vertex)
                heapq.heappush(vertex_heap, value)

    return dist[t] if dist[t] != maxsize else -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
