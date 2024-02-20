# python3
from collections import deque


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

    def __repr__(self):
        return "%s --> %s : %s" % (self.u, self.v, self.capacity)

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.


class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

    # to find a good augmenting s-t path
    # we use breadth-first-search here
    def find_augmenting_path(self, from_, to, path):

        # check visited or not to each vertex
        visited = [False] * self.size()
        vertex_que = deque()
        vertex_que.append(from_)
        visited[from_] = True
        while vertex_que:
            u = vertex_que.popleft()
            for id in self.get_ids(u):
                edge = self.get_edge(id)
                if visited[edge.v] == False and (edge.capacity - edge.flow) > 0:
                    vertex_que.append(edge.v)
                    visited[edge.v] = True
                    path[edge.v] = id
                    if edge.v == to:
                        return True

        return False

    def max_flow(self, from_, to):
        flow = 0
        path = [-1] * self.size()
        while self.find_augmenting_path(from_, to, path):

            # finding minimum capacity
            path_flow = float("Inf")
            sink = to
            while True:
                edge = self.get_edge(path[sink])
                path_flow = min((edge.capacity - edge.flow), path_flow)
                sink = edge.u
                if sink == from_:
                    break

            flow += path_flow
            sink = to
            while True:
                id = path[sink]
                self.add_flow(id, path_flow)
                edge = self.get_edge(id)
                sink = edge.u
                if sink == from_:
                    break
        return flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


if __name__ == '__main__':
    graph = read_data()
    print(graph.max_flow(0, graph.size() - 1))
