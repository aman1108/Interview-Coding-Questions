def solve(A):
    n=len(A)
    m=len(A[0])

    DP=[[0 for i in range(m+1)] for j in range(n+1)]
    ans=A[n-1][m-1]

    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            val=DP[i+1][j]+DP[i][j+1]-DP[i+1][j+1]
            DP[i][j]=A[i][j]+val
            ans=max(ans,DP[i][j])
            print(i,j,DP[i][j])

    return ans

A=[[-5,-4,-1],[-3,2,4],[2,5,8]]
print(solve(A))
