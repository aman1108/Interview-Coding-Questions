def solve(edges):
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
            rank[x]=rank[x]+1

    n=len(edges)
    rank=[0 for i in range(n+1)]
    par=[i for i in range(n+1)]
    for a,b in edges:
        x,y=find(par,a),find(par,b)
        if (x==y):
            return a,b
        union(rank,par,x,y)

print(solve([[1,2],[1,3],[2,3]]))
        
