from collections import defaultdict


def solve(stones):
    def find(par,x):
        while(x!=par[x]):
            x=par[x]
        return x

    def union(par,rank,x,y):
        if (rank[x]>rank[y]):
            par[y]=x

        elif (rank[y]>rank[x]):
            par[x]=y

        else:
            par[y]=x
            rank[x]+=1
        
    n=len(stones)
    mv=20002
    par=[i for i in range(mv+1)]
    rank=[0 for i in range(mv+1)]

    for a,b in stones:
        x=find(par,a)
        y=find(par,1001+b)
        if (x!=y):
            union(par,rank,x,y)
    
    G={}
    ans=0
    for a,b in stones:
        x=find(par,a)
        y=find(par,1001+b)
        #print(x,y)
        if x not in G:
            G[x]=1
            ans=ans+1
    return n-ans
        
#print(solve([[0,0],[0,2],[1,1],[2,0],[2,2]]))
#print(solve([[0,1],[1,0],[1,1]]))
print(solve([[0,1],[1,2],[1,3],[3,3],[2,3],[0,2]]))
''' O(n^2)
def solve(stones):
    n=len(stones)
    G=defaultdict(list)
    for i in range(n):
        for j in range(1,n):
            if (stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]):
                G[i].append(j)
                G[j].append(i)
    vis=[0 for i in range(n)]
    ans=0
    for i in range(n):
        if (vis[i]==0):
            Q=[i]
            cnt=0
            while(len(Q)!=0):
                a=Q.pop()
                vis[a]=1
                cnt=cnt+1
                for j in G[a]:
                    if (vis[j]==0):
                        vis[j]=1
                        Q.append(j)
            ans=ans+cnt-1

    return ans
'''

    
