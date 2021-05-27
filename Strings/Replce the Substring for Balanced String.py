from collections import defaultdict
def solve(s):
    n=len(s)
    G={}
    G['Q']=0
    G['W']=0
    G['E']=0
    G['R']=0

    j=0
    ans=n
    for i in range(n-1,-1,-1):
        if (G[s[i]]+1>(n/4)):
            break
        j=i
        G[s[i]]+=1

    ans=min(ans,j)
    for i in range(n):
        G[s[i]]=G[s[i]]+1
        while(j<n and G[s[i]]>(n/4)):
            G[s[j]]=G[s[j]]-1
            j=j+1

        if(G['Q']<=(n/4) and G['W'] <=(n/4) and G['E']<=(n/4) and G['R']<=(n/4)):
            ans=min(ans,j-i-1)

    return ans

print(solve("QQQW"))
