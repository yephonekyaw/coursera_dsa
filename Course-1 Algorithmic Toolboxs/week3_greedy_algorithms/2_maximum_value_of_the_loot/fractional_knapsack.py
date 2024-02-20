# Uses python3
import sys
def get_optimal_value(capacity, weights, values):
    value = 0
    #O(n)
    unit_per_lst = [values[i]/weights[i] for i in range(len(values))]
    #O(n)
    key_lst = [i[0] for i in sorted(enumerate(unit_per_lst), key=lambda x: x[1], reverse=True)]
    #O(n)
    for i in key_lst:
        if capacity <= 0:
            return value
        tem_value = min(weights[i],capacity)
        value += unit_per_lst[i]*tem_value
        capacity -= tem_value
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))