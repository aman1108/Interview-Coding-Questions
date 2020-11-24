
def solve(A,B):
    n=len(A)
    m=len(B)
    DP=[[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if (A[i-1]==B[j-1]):
                DP[i][j]=max(DP[i-1][j],DP[i][j-1],DP[i-1][j-1]+1)

            else:
                DP[i][j]=max(DP[i-1][j],DP[i][j-1],DP[i-1][j-1])

    return(DP[n][m])

print(solve("abc","abc"))
