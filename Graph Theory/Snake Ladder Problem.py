def solve(A,B):
    G={}
    for i in range(1,101):
        G[i]=[]
        for j in range(i+1,min(i+6+1,101)):
            G[i].append(j)

    N=len(A)
    M=len(B)
    for i in range(N):
        G[A[i][0]]=[A[i][1]]

    for i in range(M):
        G[B[i][0]]=[B[i][1]]

    #print(G)
    Q=[1]
    ans=0
    vis=[-1 for i in range(101)]
    vis[1]=0
    while(len(Q)!=0):
        #print(Q)
        a=Q.pop(0)
        v=vis[a]
        for i in G[a]:
            if (vis[i]==-1 or vis[i]>v+1):
                if (i>a+6 or i<a):
                    vis[i]=v
                else:
                    vis[i]=v+1
                Q.append(i)
        
    #print(vis[33])
    return(vis[100])

A = [  [8, 52],
        [6, 80],
        [26, 42],
        [2, 72]
     ]
B = [  [51, 19],
        [39, 11],
        [37, 29],
        [81, 3],
        [59, 5],
        [79, 23],
        [53, 7],
        [43, 33],
        [77, 21] ]
print(solve(A,B))
