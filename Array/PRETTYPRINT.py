def solve(A):
    n=A
    DP=[[0 for i in range((2*n)-1)] for j in range((2*n)-1)]
    
    DP[n-1][n-1]=1
    for i in range (n):
        for j in range(n):
            v=min(i,j)
            DP[i][j]=n-v
            DP[(2*(n-1))-i][j]=n-v
            DP[i][(2*(n-1))-j]=n-v
            DP[(2*(n-1))-i][(2*(n-1))-j]=n-v

    for i in range(2*n-1):
        print(*DP[i])

    return DP

solve(3)
            
