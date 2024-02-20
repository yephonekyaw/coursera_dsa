#Uses python3

import sys
from sys import maxsize
from collections import deque

def bipartite(adj):
    # declarations
    dist = [maxsize] * len(adj)
    color_lst = [None] * len(adj)
    visited = [False] * len(adj)
    vertex_queue = deque()

    # operations 
    for i in range(len(adj)):
        
        if not visited[i]:

            # first assigning to source of connected component
            if not vertex_queue:
                dist[i] = 0
                color_lst[i] = 1
                visited[i] = True
                vertex_queue.append(i)
            
            # loop the queue
            while vertex_queue:
                cur_source = vertex_queue.popleft()
                for vertex in adj[cur_source]:
                    visited[vertex] = True

                    # retrun 0 if self loop
                    if vertex == cur_source:
                        return 0

                    if dist[vertex] == maxsize and color_lst[vertex] == None:
                        dist[vertex] = dist[cur_source] + 1
                        color_lst[vertex] = 1 - color_lst[cur_source]
                        vertex_queue.append(vertex)
                    elif dist[vertex] == dist[cur_source]:
                        if color_lst[vertex] == color_lst[cur_source]:
                            return 0
    return 1

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
    print(bipartite(adj))
