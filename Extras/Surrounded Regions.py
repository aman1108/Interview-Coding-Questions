def solve(board):
    def bfs(n,m,Q,A,vis):
        while(len(Q)!=0):
            print(Q)
            x,y=Q.pop()
            vis[x][y]=1
            if (x>0 and vis[x-1][y]==0 and A[x-1][y]=="O"):
                vis[x-1][y]=1
                Q.append([x-1,y])

            if (y>0 and vis[x][y-1]==0 and A[x][y-1]=="O"):
                vis[x][y-1]=1
                Q.append([x,y-1])

            if (x<(n-1) and vis[x+1][y]==0 and A[x+1][y]=="O"):
                vis[x+1][y]=1
                Q.append([x+1,y])

            if (y<(m-1) and vis[x][y+1]==0 and A[x][y+1]=="O"):
                vis[x][y+1]=1
                Q.append([x,y+1])
                    
        
    n=len(board)
    m=len(board[0])

    vis=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        if (vis[i][0]==0 and board[i][0]=="O"):
            bfs(n,m,[[i,0]],board,vis)
        if (vis[i][m-1]==0 and board[i][m-1]=="O"):
            bfs(n,m,[[i,m-1]],board,vis)

    for i in range(m):
        if (vis[0][i]==0 and board[0][i]=="O"):
            bfs(n,m,[[0,i]],board,vis)
        if (vis[n-1][i]==0 and board[n-1][i]=="O"):
            bfs(n,m,[[n-1,i]],board,vis)

    #print(vis)
    for i in range(n):
        for j in range(m):
            if (board[i][j]=="O" and vis[i][j]==0):
                board[i][j]="X"

board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
solve(board)
print(board)
