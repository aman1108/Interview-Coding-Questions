from collections import defaultdict
def find(G,st,n):
    Q=[st[0]]
    vis=[-1 for i in range(n+1)]
    for a in st:
        vis[a]=0
    stk=[]
    cnt=0
    while(len(Q)!=0):
        a=Q.pop()
        cnt=cnt+1
        vis[a]=-1
        stk.append(a)
        for val in G[a]:
            if (vis[val]==0):
                Q.append(val)
                vis[val]=-1
    
    if (cnt!=len(st)):
        return 0
    
    stk.reverse()
    ans=0
    for a in stk:
        cnt=1
        A=[0,0]
        for val in G[a]:
            if (vis[val]!=-1):
                cnt=max(cnt,vis[val]+1)
                A.append(vis[val])
        A.sort()
        ans=max(ans,A[-1]+A[-2]+1)
        vis[a]=cnt
    return ans-1

    
def solve(n,edges):
    G=defaultdict(list)
    for a,b in edges:
        G[a].append(b)
        G[b].append(a)
    #print(G)
    ans=[0 for i in range(n)]
    for i in range(1,2**n):
        st=[]
        for j in range(n):
            if (((i>>j)&1)==1):
                st.append(j+1)
        
        val=find(G,st,n)
        ans[val]+=1
    return ans[1:]

print(solve(4,[[1,2],[2,3],[2,4]]))
                
print(solve(3,[[1,2],[2,3]]))
