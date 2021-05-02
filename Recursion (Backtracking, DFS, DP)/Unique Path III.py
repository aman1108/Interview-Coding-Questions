def solve(grid):
    n=len(grid)
    m=len(grid[0])
    st,end=[0,0],[0,0]
    empty=0
    for i in range(n):
        for j in range(m):
            if (grid[i][j]==1):
                st=[i,j]
                empty+=1
            elif (grid[i][j]==2):
                end=[i,j]
                grid[i][j]=0
                empty+=1
            elif (grid[i][j]==0):
                empty+=1
                

    
    def fun(grid,pts,cnt):
        nonlocal ans
        nonlocal empty
        if (pts==end and (cnt+1)==empty):
            ans=ans+1

        else:
            x,y=pts
            grid[x][y]=-1
            if (x>0 and grid[x-1][y]==0):
                fun(grid,[x-1,y],cnt+1)

            if (y>0 and grid[x][y-1]==0):
                fun(grid,[x,y-1],cnt+1)

            if (x<(n-1) and grid[x+1][y]==0):
                fun(grid,[x+1,y],cnt+1)

            if (y<(m-1) and grid[x][y+1]==0):
                fun(grid,[x,y+1],cnt+1)

            grid[x][y]=0

    ans=0
    fun(grid,st,0)
    return ans
                
print(solve([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(solve([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(solve([[0,1],[2,0]]))
    
