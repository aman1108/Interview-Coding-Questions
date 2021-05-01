from collections import defaultdict

def solve(n,edges):
        
    def find(par,x):
        while(x!=par[x]):
            x=par[x]
        return x

    def union(rank,par,x,y):
        if (rank[x]>rank[y]):
            par[y]=x

        elif (rank[y]>rank[x]):
            par[x]=y

        else:
            par[y]=x
            rank[x]+=1

            
    A=[]
    m=len(edges)
    for i in range(m):
        A.append([edges[i][2],edges[i][0],edges[i][1],i])

    A.sort()
    rank=[0 for i in range(n)]
    par=[i for i in range(n)]
    mst=0
    for i in range(m):
        x,y=find(par,A[i][1]),find(par,A[i][2])
        if (x!=y):
            mst=mst+A[i][0]
            union(rank,par,x,y)

    critical=[]
    for i in range(m):
        temp=0
        rank=[0 for i in range(n)]
        par=[i for i in range(n)]
        for j in range(m):
            if (i!=j):
                x,y=find(par,A[j][1]),find(par,A[j][2])
                if (x!=y):
                    temp=temp+A[j][0]
                    union(rank,par,x,y)
        if (temp!=mst):
            critical.append(A[i][3])

    pseudo=[]
    for i in range(m):
        temp=0
        rank=[0 for i in range(n)]
        par=[i for i in range(n)]
        x,y=find(par,A[i][1]),find(par,A[i][2])
        if (x!=y):
            temp=temp+A[i][0]
            union(rank,par,x,y)
        for j in range(m):
            if (i!=j):
                x,y=find(par,A[j][1]),find(par,A[j][2])
                if (x!=y):
                    temp=temp+A[j][0]
                    union(rank,par,x,y)
        if (temp==mst and A[i][3] not in critical):
            pseudo.append(A[i][3])

    ans=[critical,pseudo]
    return ans
        
                

print(solve(5,[[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))
    
print(solve(4,[[0,1,1],[1,2,1],[2,3,1],[0,3,1]]))
