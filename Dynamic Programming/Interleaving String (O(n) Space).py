def solve(s1,s2,s3):
    n=len(s1)
    m=len(s2)

    if(len(s3)!=n+m):
        return 0
    DP=[0 for i in range(m+1)] 
    DP[0]=1
    for i in range(m):
        if (s2[i]==s3[i]):
            DP[i+1]=1
        else:
            break

    for i in range(1,n+1):
        for j in range(m+1):
            if (j==0):
                DP[j]=DP[j]&(s1[i-1]==s3[i-1])
            else:
                DP[j]=DP[j]*(s1[i-1]==s3[j+i-1])
                if(s2[j-1]==s3[i+j-1]):
                    DP[j]=max(DP[j],DP[j-1])
            #print(i,j,DP)
    return DP[m]
                
                    
        
    
    
print(solve("db","b","cbb"))

'''
DP=[[0 for i in range(m+1)] for j in range(n+1)]
    DP[0][0]=1
    
    for i in range(1,n+1):
        if (s1[i-1]==s3[i-1]):
            DP[i][0]=1
        else:
            break

    for i in range(1,m+1):
        if (s2[i-1]==s3[i-1]):
            DP[0][i]=1
        else:
            break

    for i in range(1,n+1):
        for j in range(1,m+1):
            if (s1[i-1]==s3[i+j-1]):
                DP[i][j]=max(DP[i][j],DP[i-1][j])
            if(s2[j-1]==s3[i+j-1]):
                DP[i][j]=max(DP[i][j],DP[i][j-1])
                
    return DP[n][m]
'''
        
