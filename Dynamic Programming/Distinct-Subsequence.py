def solve(A,B):
    n=len(A)
    m=len(B)
    
    DP=[[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(n):
        DP[i][0]=1
    #print(DP)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (A[i-1]==B[j-1]):
                DP[i][j]=DP[i-1][j]+DP[i-1][j-1]

            else:
                #print(i,j)
                DP[i][j]=DP[i-1][j]
            
                    
    #print(DP)
    return DP[n][m]

print(solve("rabbbit","rabbit"))
