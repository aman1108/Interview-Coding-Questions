def solve(A,B):
    n=A
    m=len(B)
    G={}
    for i in range(1,n+1):
        G[i]=[]
    
    for i in B:
        G[i[0]].append(i[1])

    vism=[-1 for i in range(n+1)]
    for i in range(1,n+1):
        if(vism[i]==-1):
            vis=[-1 for i in range(n+1)]
            rstack=[-1 for i in range(n+1)]
            Q=[i]
            vism[i]=1
            while(len(Q)!=0):
                #print(Q)
                a=Q[-1]
                vism[a]=1
                rstack[a]=1
                flag=0
                for i in G[a]:
                    if (vis[i]==-1):
                        flag=1
                        Q.append(i)
                        vis[i]=1
        
                    elif(rstack[i]!=-1):
                        return 1
                if(flag==0):
                    rstack[a]=-1
                    Q.pop()
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
