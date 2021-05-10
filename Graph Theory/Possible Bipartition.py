from collections import defaultdict

def solve(N,dislikes):
    G=defaultdict(list)
    for a,b in dislikes:
        G[a].append(b)
        G[b].append(a)

    vis=[-1 for i in range(N+1)]
    for i in range(1,N+1):
        if (vis[i]==-1):
            Q=[i]
            vis[i]=0
            while(len(Q)!=0):
                a=Q.pop()
                v=vis[a]    
                for j in G[a]:
                    if (vis[j]==-1):
                        vis[j]=(v+1)%2
                        Q.append(j)

                    elif(vis[j]==v):
                        return False
    return True

print(solve(4,[[1,2],[1,3],[2,4]]))
print(solve(3,[[1,2],[1,3],[2,3]]))            
            
