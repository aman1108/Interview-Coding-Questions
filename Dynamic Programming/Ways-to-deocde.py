def solve(A):
    
    n=len(A)
    mod=(10**9)+7
    DP=[0 for i in range(n+1)]
    DP[n]=1
    
    if (A[-1]!='0'):
        DP[n-1]=1
    for i in range(n-2,-1,-1):
        if (A[i]=='0'):
            continue
            
        elif (int(A[i]+A[i+1])<27):
            DP[i]=(DP[i+1]+DP[i+2])%mod

        else:
            DP[i]=(DP[i+1])%mod

    return DP[0]

print(solve('01'))
