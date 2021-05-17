from collections import defaultdict,deque
def solve(graph):
    n=len(graph)
    cnt=[0]*n

    G=defaultdict(list)
    for i in range(n):
        for a in graph[i]:
            cnt[i]+=1
            G[a].append(i)
            
    ans=[]
    Q=deque([])
    for i in range(n):
        if (cnt[i]==0):
            Q.append(i)

    print(cnt)    
    while(len(Q)!=0):
        a=Q.popleft()
        ans.append(a)
        for v in G[a]:
            cnt[v]=cnt[v]-1
            if (cnt[v]==0):
                Q.append(v)
    return ans

print(solve([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
