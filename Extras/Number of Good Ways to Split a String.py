from collections import defaultdict
def solve(s):
    n=len(s)

    pref=[0]*n
    G=defaultdict(lambda:0)
    for i in range(n):
        G[s[i]]=1
        pref[i]=len(G)

    G=defaultdict(lambda:0)
    ans=0
    for i in range(n-1,-1,-1):
        if (len(G)==pref[i]):
            ans=ans+1
        G[s[i]]=1

    return ans

print(solve("abcd"))
