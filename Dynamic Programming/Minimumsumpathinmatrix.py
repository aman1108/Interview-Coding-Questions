def solve(A):
    n=len(A)
    m=len(A[0])
    DP=[[0 for i in range(m)] for j in range(n)]
    DP[-1][-1]=A[-1][-1]
    
    for i in range(n-2,-1,-1):
        DP[i][-1]=DP[i+1][-1]+A[i][-1]
    
    for i in range(m-2,-1,-1):
        DP[-1][i]=DP[-1][i+1]+A[-1][i]
    
    for i in range(n-2,-1,-1):
        for j in range(m-2,-1,-1):
            DP[i][j]=A[i][j]+min(DP[i+1][j],DP[i][j+1])

    print(DP)
    return DP[0][0]


A = [  [1, 3, 2],
        [4, 3, 1],
        [5, 6, 1]
     ]

print(solve(A))
    
