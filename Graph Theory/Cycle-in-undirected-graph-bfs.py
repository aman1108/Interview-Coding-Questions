def solve(A,B):
    n=A
    m=len(B)
    G={}
    for i in range(1,n+1):
        G[i]=[]
    for i in range(m):
        G[B[i][0]].append(B[i][1])
        G[B[i][1]].append(B[i][0])

    vism=[0 for i in range(n+1)]
    par=[0 for i in range(n+1)]
    for i in range(1,n+1):
        if (vism[i]==0):
            Q=[i]
            vis=[0 for i in range(n+1)]
            while(len(Q)!=0):
                print(Q)
                a=Q.pop()
                vism[i]=1
                vis[a]=1
                for i in G[a]:
                    if (i!=par[a] and vis[i]!=0):
                        return 1
                    elif(vis[i]==0):
                        Q.append(i)
                        vis[i]=1
                        par[i]=a

    return 0
                        
A=2
B=[[1,2]]
print(solve(A,B))
