def solve(A,B):
    n=A
    m=len(B)
    G={}
    for i in range(1,n+1):
        G[i]=[]

    indeg=[0 for i in range(n+1)]
    
    for i in B:
        G[i[0]].append(i[1])
        indeg[i[1]]+=1

    Q=[]
    for i in range(1,n+1):
        if (indeg[i]==0):
            Q.append(i)

    vis=[0 for i in range(n+1)]
    while(len(Q)!=0):
        a=Q.pop()
        vis[a]=1
        for i in G[a]:
            if (vis[i]==0):
                indeg[i]-=1
                if (indeg[i]==0):
                    Q.append(i)
    for i in range(1,n+1):
        if (vis[i]==0):
            return 1
    return 0

    

A = 5
B =[
  [1, 2],
  [1, 3],
  [2, 3],
  [1, 4],
  [4, 3],
  [4, 5],
  [3, 5]
]
print(solve(A,B))
A = 5
B = [  [1, 2] ,
        [3, 1] ,
        [2, 3] ,
        [3, 4] ,
        [5, 2] ,
        [1, 3] ]
print(solve(A,B))
A = 5
B = [  [1, 2],
        [2, 3] ,
        [3, 4] ,
        [4, 5] ]
print(solve(A,B))
