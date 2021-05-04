def solve(s):
    if (s[0]=="0"):
        return 0
    
    n=len(s)
    DP=[0]*n
    G={str(i) for i in range(1,27)}
    
    DP[0]=1
    for i in range(1,n):
        if s[i] in G:
            DP[i]=DP[i]+DP[i-1]
        if (s[i-1]+s[i]) in G:
            if (i>1):
                DP[i]=DP[i]+DP[i-2]
            else:
                DP[i]=DP[i]+1
    return DP[n-1]

print(solve("06"))
        
            
