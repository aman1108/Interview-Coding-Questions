from collections import defaultdict
def solve(nums):
    n=len(nums)
    G=defaultdict(list)

    for a,b in nums:
        G[a].append(b)
        G[b].append(a)

    Q=[]
    for v in G:
        if (len(G[v])==1):
            Q=[v]
            break

    ans=[]
    s=set()
    while(len(Q)!=0):
        a=Q.pop()
        ans.append(a)
        s.add(a)
        for b in G[a]:
            if b not in s:
                Q.append(b)
    return ans

print(solve([[2,1],[3,4],[3,2]]))
        
    
