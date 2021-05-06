def solve(s):
    G={}
    bmask=0
    ans=0
    G[0]=0
    for i in range(len(s)):
        v=int(s[i])
        bmask=bmask^(1<<v)

        for j in range(10):
            val= bmask^(1<<j)
            if val in G:
                ans=max(ans,i-G[val]+1)
            
        if bmask in G:
            ans=max(ans,i-G[bmask]+1)
        else:
            G[bmask]=i+1
    return ans

print(solve("76263"))

print(solve("11111"))   
print(solve("213123"))
