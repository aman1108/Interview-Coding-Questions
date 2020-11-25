def isScramble(A,B):
    n=len(A)
    DP=[[[0 for i in range(n)] for j in range(n)] for k in range(n+1)]

    for l in range(1,n+1):
        for i in range(n-l+1):
            if (l==1):
                for j in range(n):
                    if (A[i]==B[j]):
                        DP[l][i][j]=1
                    continue
            else:
                for j in range(n-l+1):
                    a1,b1=i,i+l-1
                    a2,b2=j,j+l-1
                    for k in range(1,l):
                        a,b=k,l-k
                        DP[l][i][j]=min(DP[a][a1][a2],DP[b][a1+a][a2+a])
                        DP[l][i][j]=max(DP[l][i][j],min(DP[a][a1][b2-a+1],DP[b][a1+a][a2]))
                        if(DP[l][i][j]==1):
                            break
    #for l in range(n+1):
        #print(DP[l])
    for i in range(n-1):
        
        if (DP[i+1][0][0]==1 and DP[n-i-1][i+1][i+1]==1):
            return 1
        if (DP[i+1][0][n-i-1]==1 and DP[n-i-1][i+1][0]==1):
            return 1

    return 0
                        
                        
                
print(isScramble("aabaa","aaaab"))
                    
        
