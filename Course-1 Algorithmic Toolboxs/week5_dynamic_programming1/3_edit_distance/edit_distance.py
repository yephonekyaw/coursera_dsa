# Uses python3
def edit_distance(s, t):
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    align_T = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    for i in range(len(s)+1):
        d[i][0]=i
        align_T[i][0]=i
    for j in range(len(t)+1):
        d[0][j]=j
        align_T[0][j]=j
    
    for j in range(1, len(t)+1):
        for i in range(1, len(s)+1):
            insertion = d[i][j-1]+1
            delection = d[i-1][j]+1
            match = d[i-1][j-1]
            mismatch = d[i-1][j-1]+1
            if s[i-1]==t[j-1]:
                d[i][j] = min(insertion,delection,match)
            else:
                d[i][j] = min(insertion,delection,mismatch)
    
    return d[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
