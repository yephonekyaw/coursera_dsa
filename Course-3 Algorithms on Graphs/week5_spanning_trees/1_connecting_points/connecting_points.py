#Uses python3
import sys
import math
import heapq

def minimum_distance(x, y):
    result = 0.
    
    # I'll use Prim's Algorithm
    # first declaration
    distance = [float('inf')] * len(x)
    parent = [None] * len(x)
    vertex_in_heap = [True] * len(x) 
    vertex_heap = []

    # first declaration
    # choose arbitrary source vertex
    # I choose zero as a root
    distance[0] = 0
    for i in range(len(x)):
        value = (float('inf'), i)
        if i == 0:
            value = (0, i)
        heapq.heappush(vertex_heap, value)

    # operations
    while vertex_heap:
        minimum_distance, source_vertex = heapq.heappop(vertex_heap)
        vertex_in_heap[source_vertex] = False
        for i in range(len(x)):
            if i != source_vertex and vertex_in_heap[i]:
                x_ = float("{0:.9f}".format((x[source_vertex] - x[i])**2))
                y_ = float("{0:.9f}".format((y[source_vertex] - y[i])**2))
                cost = float("{0:.9f}".format(math.sqrt(x_ + y_)))
                if distance[i] > cost:
                    distance[i] = cost
                    parent[i] = source_vertex
                    value = (cost, i)
                    heapq.heappush(vertex_heap, value)
    result = sum(distance)

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
