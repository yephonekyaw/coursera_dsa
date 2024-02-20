# python3

def max_matching(graph):
    N = len(graph)
    ymatch = [-1] * N
    seen = []

    def dfs(i):
        if seen[i]:
            return 0
        
        seen[i] = 1
        for j in range(N):
            if graph[i][j] and ((ymatch[j] == -1) or dfs(ymatch[j])):
                ymatch[j] = i
                return 1
        return 0
    
    res = 0
    for i in range(N):
        seen = [0] * N
        res += dfs(i)
    return res

def Less(a, b):
    assert len(a) == len(b)
    return all(a[i] < b[i] for i in range(len(a)))

if __name__ == '__main__':
    N, K = map(int, input().split())
    stock_data = [list(map(int, input().split())) for _ in range(N)]
    graph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if Less(stock_data[i], stock_data[j]):
                graph[i][j] = 1
    
    print(N - max_matching(graph))

