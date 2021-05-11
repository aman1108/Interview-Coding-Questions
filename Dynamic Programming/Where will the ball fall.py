def solve(grid):
    n=len(grid)
    m=len(grid[0])
    
    for i in range(n):
        for j in range(m-1):
            if (grid[i][j]==1 and grid[i][j+1]==-1):
                grid[i][j]=0
                grid[i][j+1]=0
    
    ans=[-1]*m
    for i in range(m):
        v=grid[0][i]
        cur=i
        flag=0
        if (v==0):
            flag=1
        for j in range(1,n):
            cur=cur+v
            #print(cur,v)
            if (cur<0 or cur>=m or grid[j][cur]==0):
                flag=1

            if(flag==1):
                break
            v=grid[j][cur]
            
        if(flag==0 and cur+v>=0 and cur+v<m):
            ans[i]=cur+v
    return ans

print(solve([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))

print(solve( [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
#print(solve( [[-1]]))

#print(solve([[-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1]]))       
            
