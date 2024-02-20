# with adjacency list
from collections import defaultdict


class Graph:

    def __init__(self, graph):

        self.graph = graph  # residual graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False]*(self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        return False

    def FordFulkerson(self, source, sink):
        parent = [-1]*(self.ROW)
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


# Create a graph given in the above diagram
if __name__ == "__main__":
    vertex_count, edge_count = map(int, input().split())
    graph = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph[u - 1][v - 1] = capacity
        graph[v - 1][u - 1] = 0

    g = Graph(graph)
    print(graph)
    source = 0
    sink = vertex_count - 1
    # print("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
