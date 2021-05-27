from collections import defaultdict
def solve(s):
    n=len(s)
    G=["0","1"]

    cur=0
    ans=0
    for i in range(n):
        if (s[i]!=G[cur]):
            ans=ans+1
            cur=(cur+1)%2

    return ans

print(solve("001011101"))
    
    
    
