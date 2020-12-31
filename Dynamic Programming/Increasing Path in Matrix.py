def solve(A):
    n=len(A)
    m=len(A[0])

    DP=[[1 for i in range(m)] for j in range(n)]

    ans=0
    for i in range(n-1,0,-1):
        for j in range(m-1,0,-1):
            if (A[i][j]>A[i-1][j]):
                DP[i-1][j]=max(DP[i-1][j],DP[i][j]+1)

            if (A[i][j]>A[i][j-1]):
                DP[i][j-1]=max(DP[i][j-1],DP[i][j]+1)

    
    for i in range(n-1,-1,-1):
        if (A[i][0]>A[i-1][0]):
            DP[i-1][0]=max(DP[i-1][0],DP[i][0]+1)

    for i in range(m-1,-1,-1):
        if (A[0][i]>A[0][i-1]):
            DP[0][i-1]=max(DP[0][i]+1,DP[0][i-1])

    if (DP[0][0]!=(n+m-1)):
        ans=-1
    else:
        ans=DP[0][0]
    return ans

A=[  [1, 2, 3, 4],
        [2, 2, 3, 4],
        [3, 2, 3, 4],
        [4, 5, 6, 7]
     ]

A=[
  [35, 1, 70, 25, 79, 59, 63, 65],
  [6, 46, 82, 28, 62, 92, 96, 43]
]
print(solve(A))


    
        
