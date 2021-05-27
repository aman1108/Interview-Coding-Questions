from collections import defaultdict
def solve(s):
    n=len(s)

    pref=[1]*n
    
    G=defaultdict(lambda:-1)

    for i in range(n):
        pref[i]=i-G[s[i]]
        G[s[i]]=i

    ans=0
    mod=(10**9)+7
    G=defaultdict(lambda:n)
    
    for i in range(n-1,-1,-1):
        val=G[s[i]]-i
        ans=(ans+(val*pref[i]))%mod
        G[s[i]]=i

    return ans

print(solve("LEETCODE"))
