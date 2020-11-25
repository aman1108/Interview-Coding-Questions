def solve(A):
    n=len(A)
    m=len(A[0])
    vis=[[0 for i in range(m)] for j in range(n)]
    
    for i in range(n):
        for j in range(m):
            if (vis[i][j]==0 and A[i][j]==1):
                Q=[[i,j]]
                vis[i][j]=1
                c,p=2,A[i][j]
                while(len(Q)!=0):
                    a,b=Q.pop()
                    #print(a,b,p,Q)
                    p1=[0,-1,1]
                    p2=[0,-1,1]
                    for ik in p1:
                        for jk in p2:
                            if (a+ik>=0 and a+ik<n and b+jk>=0 and b+jk<m and vis[a+ik][b+jk]==0 and A[a+ik][b+jk]==p):
                                vis[a+ik][b+jk]=c
                                Q.append([a+ik,b+jk])
                                c=c+1
    ans=0
    for i in range(n):
        ans=max(ans,max(vis[i]))

    return ans

A=[
  [1, 0],
  [1, 1],
  [0, 0],
  [0, 0],
  [0, 0],
  [1, 0],
  [0, 1]
]
print(solve(A))
