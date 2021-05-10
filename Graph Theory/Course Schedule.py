from collections import deque,defaultdict

def solve(numCourses,prerequisites):
    n=len(prerequisites)
    G=defaultdict(list)
    vis=[0 for j in range(numCourses)]
    for i in range(n):
        a,b=prerequisites[i]
        G[b].append(a)
        vis[a]+=1
        
    Q=deque([])    
    for i in range(numCourses):
        if (vis[i]==0):
            Q.append(i)
    cnt=0
    while(len(Q)!=0):
        a=Q.popleft()
        cnt+=1
        for v in G[a]:
            vis[v]=vis[v]-1
            if (vis[v]==0):
                Q.append(v)
    if (cnt==numCourses):
        return True
    return False
