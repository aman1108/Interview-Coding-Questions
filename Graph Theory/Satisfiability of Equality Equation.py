def solve(equations):
    def find(x,par):
        while(x!=par[x]):
            x=par[x]
        return x

    def union(par,rank,x,y):
        if (rank[x]>rank[y]):
            par[y]=x

        elif(rank[x]<rank[y]):
            par[x]=y

        else:
            par[y]=x
            rank[x]+=1
            
    n=len(equations)
    par=[i for i in range(27)]
    rank=[0 for i in range(27)]

    for s in equations:
        if (s[1]=="="):
            a,b=ord(s[0])-97,ord(s[-1])-97
            x,y=find(a,par),find(b,par)
            union(par,rank,x,y)

    for s in equations:
        if (s[1]!="="):
            a,b=ord(s[0])-97,ord(s[-1])-97
            x,y=find(a,par),find(b,par)
            if (x==y):
                return False
    return True

print(solve(["a==b","z!=a"]))
    
