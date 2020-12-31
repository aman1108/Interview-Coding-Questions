#problem:https://www.interviewbit.com/problems/maximum-size-square-sub-matrix/
def solve(A):
    n=len(A)
    m=len(A[0])

    DP=[[[0,0] for i in range(m+1)] for j in range(n+1)]

    ans=0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if (A[i-1][j-1]==1):
                DP[i][j][0]=min(DP[i-1][j-1][0],DP[i-1][j][0],DP[i][j-1][0])+1
                DP[i][j][1]=min(DP[i-1][j-1][1],DP[i-1][j][1],DP[i][j-1][1])+1

            if (DP[i][j][0]==DP[i][j][1]):
                ans=max(ans,DP[i][j][0]*DP[i][j][1])
    return ans

A=[
        [0, 1, 1, 0, 1],

        [1, 1, 0, 1, 0],

        [0, 1, 1, 1, 0],

        [1, 1, 1, 1, 0],

        [1, 1, 1, 1, 1],

        [0, 0, 0, 0, 0]
     ]

#A=[[1,1],[1,1]]
print(solve(A))
