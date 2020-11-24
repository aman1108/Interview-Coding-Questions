def solve(A):
    n=len(A)
    DP=[[0 for i in range(n)] for j in range(n)]

    DP[n-1][n-1]=1
    ans=0
    for i in range(n-2,-1,-1):
        for j in range(n):
            if(j<i):
                DP[i][j]=0
            elif(i==j):
                DP[i][j]=1
            elif (A[i]==A[j]):
                #print(i,j)
                DP[i][j]=max(DP[i+1][j],DP[i][j-1],DP[i+1][j-1]+2)

            else:
                DP[i][j]=max(DP[i+1][j-1],DP[i+1][j],DP[i][j-1])
        ans=max(DP[i])
    
    return(ans)

print(solve("bebeeed"))
