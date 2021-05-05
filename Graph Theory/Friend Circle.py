def solve(isConnected):
    n=len(isConnected)
    vis=[0 for i in range(n)]
    ans=0
    for i in range(n):
        if (vis[i]==0):
            Q=[i]
            ans=ans+1
            while(len(Q)!=0):
                a=Q.pop()
                vis[a]=1
                for j in range(n):
                    if (isConnected[a][j]==1 and vis[j]==0):
                        Q.append(j)
                        vis[j]=1

    return ans

print(solve([[1,0,0],[0,1,0],[0,0,1]]))
