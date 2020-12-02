def solve(A):
    n=len(A)
    m=len(A[0])

    vis=[[1 for i in range(m+1)] for j in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if (A[i][j]=='X'):
                vis[i][j]=0

    cnt=0

    for i in range(n):
        for j in range(m):
            if (vis[i][j]==0):
                cnt=cnt+1
                Q=[[i,j]]
                while(len(Q)!=0):
                    x,y=Q.pop()

                    if (vis[x-1][y]==0):
                        Q.append([x-1,y])
                        vis[x-1][y]=1

                    if (vis[x][y-1]==0):
                        Q.append([x,y-1])
                        vis[x][y-1]=1

                    if (vis[x+1][y]==0):
                        Q.append([x+1,y])
                        vis[x+1][y]=1

                    if (vis[x][y+1]==0):
                        Q.append([x,y+1])
                        vis[x][y+1]=1

                    
    return cnt

A = [ 'OOOXOOO',
          'OOXXOXO',
          'OXOOOXO'  ]

print(solve(A))

