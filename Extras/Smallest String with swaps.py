from collections import defaultdict, deque

def solve(s,pairs):
    n=len(pairs)
    G=defaultdict(list)

    s=list(s)
    for a,b in pairs:
        G[a].append(b)
        G[b].append(a)

    vis=[0 for i in range(len(s))]

    for i in range(len(s)):
        if (vis[i]==0):
            arr=[]
            ind=[]
            Q=[i]
            while(len(Q)!=0):
                a=Q.pop()
                arr.append(s[a])
                ind.append(a)
                vis[a]=1
                for b in G[a]:
                    if (vis[b]==0):
                        vis[b]=1
                        Q.append(b)

            arr.sort()
            ind.sort()

            for i in range(len(arr)):
                s[ind[i]]=arr[i]
    
    ans=""
    for v in s:
        ans=ans+v
    return ans

print(solve("dcab",[[0,3],[1,2]]))
            
    
