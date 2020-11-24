def solve(A,S):
    n=len(A)
    m=len(S)

    B=""
    flag=0
    c=0
    for i in range(m):
        if (S[i]!='*'):
            c=c+1
            B=B+S[i]
            flag=0
        else:
            if (flag==0):
                B=B+S[i]
                flag=1
    m=len(B)
            
    print(B)
    if (c>n):
        return 0

    DP=[[0 for i in range(m+1)] for j in range(n+1)]
    
    for i in range(m):
        if (B[i]=='*'):
            DP[0][i+1]=1
        else:
            break
            
    DP[0][0]=1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if (B[j-1]=='*'):
                DP[i][j]=max(DP[i-1][j-1],DP[i-1][j],DP[i][j-1])

            elif (A[i-1]==B[j-1] or B[j-1]=='?'):
                DP[i][j]=DP[i-1][j-1]

    print(DP)
    return(DP[n][m])
    

                
print(solve("aa","***??"))
