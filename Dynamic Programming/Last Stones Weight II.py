def solve(stones):
    n=len(stones)
    s=sum(stones)
    DP=[0 for i in range((s//2)+1)]

    ans=s
    DP[0]=1
    for i in range(n):
        for j in range((s//2)-stones[i],-1,-1):
            if (DP[j]==1):
                DP[j+stones[i]]=1
                ans=min(ans,abs(s-(2*(j+stones[i]))))
    print(DP)
    return ans

print(solve([31,26,33,21,40]))
    
