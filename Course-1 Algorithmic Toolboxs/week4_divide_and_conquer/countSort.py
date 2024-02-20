# this is not working for array including zeros
def countSort(ar):
    count = [0] * (len(ar) + 1)
    for i in range(len(ar)):
        count[ar[i]] = count[ar[i]] + 1
    
    pos = [0] * len(count)
    pos[1] = 1
    for i in range(2, len(count)):
        pos[i] = pos[i-1] + count[i-1]

    res = [0] * len(ar)
    for i in range(len(ar)):
        index = pos[ar[i]] - 1
        res[index] = ar[i]
        pos[ar[i]] += 1
    
    print(res)

A = [1,1,3,3,2,3,2,2,2,3]
countSort(A)