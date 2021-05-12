def solve(p):
    n=len(p)
    DP=[0 for i in range(26)]

    cur=ord(p[n-1])-97
    cnt=1
    DP[cur]=1
    for i in range(n-2,-1,-1):
        val=ord(p[i])-97
        if ((val+1)%26==cur):
            cnt=cnt+1
            
        else:
            cnt=1
        
        DP[val]=max(DP[val],cnt)
        cur=val
    return sum(DP)
    


    
print(solve("cac"))
