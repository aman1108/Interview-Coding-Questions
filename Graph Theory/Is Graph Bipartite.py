from collections import defaultdict, deque
def solve(graph):
    n=len(graph)
    vis=[-1 for i in range(n)]

    for i in range(n):
        if (vis[i]==-1):
            Q=[i]
            vis[i]=0
            while(len(Q)!=0):
                a=Q.pop()
                for b in graph[a]:
                    if (vis[b]==-1):
                        vis[b]=(vis[a]+1)%2
                        Q.append(b)

                    elif(vis[a]==vis[b]):
                        return 0
    return 1

print(solve([[1],[0],[]]))

                    
