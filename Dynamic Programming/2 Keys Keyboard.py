def solve(n):
    DP=[i for i in range(n+1)]
    DP[1]=0
    for i in range(1,n):
        cnt=2
        for j in range(i+i,n+1,i):
            DP[j]=min(DP[j],DP[i]+cnt)
            cnt=cnt+1

    return DP[-1]

print(solve(10))
            
