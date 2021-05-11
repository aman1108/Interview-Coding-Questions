def solve(m,n):
    DP=[1 for i in range(m)]
    for i in range(1,n):
        for j in range(1,m):
            DP[j]=DP[j-1]+DP[j]

    return DP[m-1]
