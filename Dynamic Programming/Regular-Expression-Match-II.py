def solve(A,S):
    n=len(A)
    m=len(S)

    B=""
    flag=1

    for i in range(m):
        if (S[i]!='*'):
            B=B+S[i]
            flag=0
        else:
            if (flag==0):
                B=B+S[i]
                flag=1
    m=len(B)
            
    #print(B)

    DP=[[0 for i in range(m+1)] for j in range(n+1)]

    c=0
    for i in range(m):
        if (B[i]!='*'):
            c=c+1
        else:
            DP[0][i+1]=1
        if (c>=2):
            break
        
        
    DP[0][0]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (B[j-1]=='*'):
                #print(i,j,A[i-1],B[j-1],B[j-2])
                v=B[j-2]
                if (A[i-1]==v or v=='.'):
                    DP[i][j]=max(DP[i-1][j-1],DP[i][j-1],DP[i-1][j])
                DP[i][j]=max(DP[i][j],DP[i][j-2])

            elif(B[j-1]==A[i-1] or B[j-1]=='.'):
                DP[i][j]=DP[i-1][j-1]


    print(DP)
    return DP[n][m]

print(solve("ac","ab*c"))
