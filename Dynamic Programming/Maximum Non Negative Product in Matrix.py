def solve(grid):
    n=len(grid)
    m=len(grid[0])
    mod=(10**9)+7
    DP=[[0,0] for i in range(m)]
    DP[0][0],DP[0][1]=grid[0][0],grid[0][0]
    for i in range(1,m):
        DP[i][0]=min(DP[i-1][0]*grid[0][i],DP[i-1][1]*grid[0][i])
        DP[i][1]=max(DP[i-1][0]*grid[0][i],DP[i-1][1]*grid[0][i])

    
    for i in range(1,n):
        for j in range(m):
            if (j>0):
                DP[j][0],DP[j][1]=min(DP[j-1][0]*grid[i][j],DP[j-1][1]*grid[i][j],DP[j][0]*grid[i][j],DP[j][1]*grid[i][j]),max(DP[j-1][0]*grid[i][j],DP[j-1][1]*grid[i][j],DP[j][0]*grid[i][j],DP[j][1]*grid[i][j])
            else:
                DP[j][0],DP[j][1]=min(DP[j][0]*grid[i][j],DP[j][1]*grid[i][j]),max(DP[j][0]*grid[i][j],DP[j][1]*grid[i][j])
                
    ans=max(DP[-1])
    if(ans<0):
        return -1
    else:
        return ans%mod

print(solve([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))
print(solve([[1,-2,1],
               [1,-2,1],
               [3,-4,1]]))
