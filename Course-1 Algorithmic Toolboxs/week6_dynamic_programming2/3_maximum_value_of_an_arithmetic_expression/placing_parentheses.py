# Uses python3
import sys
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    for i in range(0, len(d)):
        d_min[i][i] = d[i]
        d_max[i][i] = d[i]
    
    for s in range(1, len(d)):
        for i in range(0, len(d)-s):
            j = i+s
            d_min[i][j],d_max[i][j] = MinAndMax(i,j)

def MinAndMax(i,j):
    cur_min = sys.maxsize
    cur_max = -sys.maxsize
    for k in range(i,j):
        a = evalt(d_max[i][k], d_max[k+1][j], op[k])
        b = evalt(d_max[i][k], d_min[k+1][j], op[k])
        c = evalt(d_min[i][k], d_max[k+1][j], op[k])
        d = evalt(d_min[i][k], d_min[k+1][j], op[k])
        cur_min = min(cur_min,a,b,c,d)
        cur_max = max(cur_max,a,b,c,d)
    return cur_min,cur_max

if __name__ == "__main__":
    dataset = input()
    d = list(map(int, dataset[::2]))
    op = list(dataset[1::2])
    d_min = [[0 for j in range(len(d))] for i in range(len(d))]
    d_max = [[0 for j in range(len(d))] for i in range(len(d))]
    get_maximum_value(dataset)
    print(d_max[0][len(d)-1])