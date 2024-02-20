#Uses python3
import sys
import math

def Find(i, parent):
    while i != parent[i]:
        i = parent[i]
    return i

def Union(u, v, rank, parent):
    u_id = Find(u, parent)
    v_id = Find(v, parent)

    if u_id == v_id:
        return False
    
    if rank[u_id] > rank[v_id]:
        parent[v_id] = u_id
    else:
        parent[u_id] = v_id
        if rank[u_id] == rank[v_id]:
            rank[v_id] = rank[v_id] + 1

def clustering(x, y, k):
    
    # I will use Kruskal's Algorithm
    # but need to update some stuffs
    # fristly, we need to construct a MST Tree for all edges
    # in non-decreasing order, and then cut the largest weighted edge
    # for 'k-1' times (0th, 1th, k-2, k-1)
    # as an example, if k(clusters) = 2 then we can cut only one edge to
    # get 2 clusters so we need to cut the largest edges for 'k-1' times
    # for 0-based array, it is 'k-2'
    # 0th largest weight is the largest in MST
    # 1th largest weight is the second-largest in MST
    # the 'k-1'th largest weighted edge is the minimum-required weight 
    # for all edges that are connected from one set to another and are not
    # included in MST

    # declarations
    parent = [i for i in range(len(x))]
    rank = [0] * len(x)
    sorted_weights = [] # to store (u, v, w) in non-decreasing order
    current_MST = []

    # compute the weights first
    for u in range(len(x)):
        for v in range(u+1, len(x)):
            x_ = float("{0:.9f}".format((x[u] - x[v])**2))
            y_ = float("{0:.9f}".format((y[u] - y[v])**2))
            w_ = float("{0:.9f}".format(math.sqrt(x_ + y_)))
            edge = (u, v, w_)
            sorted_weights.append(edge)

    # sort the weights in non-decreasing order
    sorted_weights = sorted(sorted_weights, key=lambda edges:edges[2])
    
    # constructing MST
    for (u, v, w) in sorted_weights:
        if Find(u, parent) != Find(v, parent):
            current_MST.append((u, v, w))
            Union(u, v, rank, parent)

    # sorted the current MST in increasing weight order
    current_MST = sorted(current_MST, key=lambda edges:edges[2], reverse=True)

    return current_MST[k-2][2]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
