from collections import defaultdict
def solve(s,t):
    n=len(s)
    m=len(t)
    G=defaultdict(lambda:0)
    H=defaultdict(lambda:0)
    for i in t:
        G[i]=G[i]+1
    cnt=0
    
    j=0
    ans=[]
    for i in range(n):
        if (G[s[i]]>H[s[i]]):
            cnt=cnt+1

        H[s[i]]=H[s[i]]+1
        if (cnt==m):
            while (H[s[j]]>G[s[j]]):
                H[s[j]]=H[s[j]]-1
                j=j+1
            ans.append([i-j,i,j])

    if (len(ans)==0):
        return ""
    mv,i,j=min(ans)
    ans=""
    for val in s[j:i+1]:
        ans=ans+val
    return ans

#print(solve("ADOBECODEBANC","ABC"))
print(solve("a","b"))
            
        
