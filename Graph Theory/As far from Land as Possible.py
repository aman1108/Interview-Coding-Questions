from collections import deque
def solve(grid):
    n=len(grid)
    Q=deque([])

    for i in range(n):
        for j in range(n):
            if (grid[i][j]==1):
                Q.append([i,j])

    ans=-1

    if (len(Q)==(n*n)):
        return -1
    while(len(Q)!=0):
        a,b=Q.popleft()
        val=grid[a][b]
        ans=max(ans,grid[a][b]-1)

        if (a>0 and grid[a-1][b]==0):
            Q.append([a-1,b])
            grid[a-1][b]=val+1

        if (b>0 and grid[a][b-1]==0):
            Q.append([a,b-1])
            grid[a][b-1]=val+1

        if (a<(n-1) and grid[a+1][b]==0):
            Q.append([a+1,b])
            grid[a+1][b]=val+1

        if (b<(n-1) and grid[a][b+1]==0):
            Q.append([a,b+1])
            grid[a][b+1]=val+1
    return ans

print(solve([[1,0],[0,1]]))
