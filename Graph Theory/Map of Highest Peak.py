from collections import deque

def solve(isWater):
    n=len(isWater)
    m=len(isWater[0])

    vis=[[-1 for i in range(m)] for j in range(n)]
    Q=deque([])
    for i in range(n):
        for j in range(m):
            if (isWater[i][j]==1):
                vis[i][j]=0
                Q.append([i,j])

    while(len(Q)!=0):
        x,y=Q.popleft()
        val=vis[x][y]
        if (x>0 and vis[x-1][y]==-1):
            vis[x-1][y]=val+1
            Q.append([x-1,y])
            
        if (y>0 and vis[x][y-1]==-1):
            vis[x][y-1]=val+1
            Q.append([x,y-1])
            
        if (x<(n-1) and vis[x+1][y]==-1):
            vis[x+1][y]=val+1
            Q.append([x+1,y])
            
        if (y<(m-1) and vis[x][y+1]==-1):
            vis[x][y+1]=val+1
            Q.append([x,y+1])
    return vis

print(solve([[0,1,0,0,0]]))
    
