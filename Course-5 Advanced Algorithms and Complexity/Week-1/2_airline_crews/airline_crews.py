# python3
from collections import deque


class MaxCrewMatching():

    def __init__(self):
        self.graph = None
        self.max_crew_matching = None
        self.from_ = 0
        self.to = -1
        self.planes = -1

    def read_data(self):
        n, m = map(int, input().split())
        self.planes = n
        self.to = n + m + 1
        self.graph = {i: {} for i in range(self.to + 1)}
        self.max_crew_matching = [-1] * self.planes

        for j in range(1, n + 1):
            crews = list(map(int, input().split()))
            # from source to u and backward
            self.graph[0][j] = 1
            self.graph[j][0] = 0
            for k in range(len(crews)):
                index = n + k + 1
                if crews[k] == 1:
                    # from u to v and backward
                    self.graph[j][index] = crews[k]
                    self.graph[index][j] = 0

                # from v to sink and backward
                self.graph[index][self.to] = 1
                self.graph[self.to][index] = 0

    def size(self):
        return len(self.graph)

    def add_flow(self, u, v, flow):
        self.graph[u][v] -= flow
        self.graph[v][u] += flow

    def find_augmenting_path(self, parent):
        visited = [False] * self.size()
        vertex_que = deque()
        vertex_que.append(self.from_)
        visited[self.from_] = True
        while vertex_que:
            u = vertex_que.popleft()
            for vertex, cap in self.graph[u].items():
                if visited[vertex] == False and cap > 0:
                    vertex_que.append(vertex)
                    visited[vertex] = True
                    parent[vertex] = u
                    if vertex == self.to:
                        return True
        
        return False

    def solve(self):
        self.read_data()
        parent = [-1] * self.size()
        while self.find_augmenting_path(parent):
            path_flow = float("Inf")
            sink = self.to
            while sink != self.from_:
                path_flow = min(path_flow, self.graph[parent[sink]][sink])
                sink = parent[sink]

            v = self.to
            while v != self.from_:
                u = parent[v]
                self.add_flow(u, v, path_flow)
                # assigning crew index to 
                # corresponding airplane
                if u != self.from_ and v != self.to:
                    if u < v:
                        self.max_crew_matching[u - 1] = v - self.planes
                v = parent[v]

        return " ".join(list(map(str, self.max_crew_matching)))

if __name__ == '__main__':
    max_matching = MaxCrewMatching()
    print(max_matching.solve())
