
def solve(grid):
    def find(DP,i,j,m):
        if (i<0 or i>m-1 or j<0 or j>m-1):
            return 0 
        return DP[i][j]
        
    n=len(grid)
    m=len(grid[0])

    DP=[[0 for i in range(m)] for j in range(m)]
    for k in range(n-1,-1,-1):
        DP1=[[0 for i in range(m)] for j in range(m)]
        for i in range(m):
            for j in range(m):
                val=grid[k][i]+grid[k][j]
                if (i==j):
                    val=grid[k][i]

                DP1[i][j]=max(find(DP,i,j,m),find(DP,i,j-1,m),find(DP,i,j+1,m))
                DP1[i][j]=max(DP1[i][j],find(DP,i-1,j,m),find(DP,i-1,j-1,m),find(DP,i-1,j+1,m))
                DP1[i][j]=max(DP1[i][j],find(DP,i+1,j,m),find(DP,i+1,j-1,m),find(DP,i+1,j+1,m))
                DP1[i][j]=DP1[i][j]+val
        DP=[[DP1[i][j] for i in range(m)] for j in range(m)]
    return DP[0][m-1]

#print(solve([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
                    
print(solve([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))
print(solve([[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]))
print(solve([[1,1],[1,1]]))
