#https://www.interviewbit.com/problems/two-teams/
def solve(A,B):
    G={}
    n=A

    for i in range(1,n+1):
        G[i]=[]
    for i in range(len(B)):
        try:
            G[B[i][0]].append(B[i][1])
        except:
            G[B[i][0]]=[B[i][1]]
        try:
            G[B[i][1]].append(B[i][0])
        except:
            G[B[i][1]]=[B[i][0]]

    print(G)
    vis=[0 for i in range(n+1)]
    par=[0 for i in range(n+1)]
    for j in range(1,n+1):
        if (vis[j]==0):
            Q=[j]
            vis[j]=1
            while(len(Q)!=0):
                a=Q.pop()
                for i in G[a]:
                    if (vis[i]==0):
                        par[i]=a
                        vis[i]=vis[a]+1
                        Q.append(i)
                    else:
                        if (i!=par[a] and (vis[i]%2)==(vis[a]%2)):
                            return 0
    return 1

A=11
B=[
  [8, 7],
  [8, 6],
  [8, 2],
  [4, 9],
  [11, 10],
  [5, 10],
  [1, 10],
  [3, 7],
  [3, 6],
  [11, 7],
  [5, 7],
  [1, 6],
  [3, 2],
  [8, 9],
  [4, 10],
  [5, 6],
  [4, 7],
  [4, 6]
]

#A=5
#B=[[1,4],[3,1],[4,3],[2,1]]

#A=6
#B=[[2,3],[2,6],[5,6],[2,4]]
print(solve(A,B))
            

    
            
