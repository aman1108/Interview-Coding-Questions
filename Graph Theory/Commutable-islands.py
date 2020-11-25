def find(x,par):
    while(x!=par[x]):
        x=par[x]
    return x

def union(x,y,rank,par):
    a,b=rank[x],rank[y]
    if (a==b):
        par[x]=y
        rank[y]=rank[y]+1

    elif(a>b):
        par[y]=x

    else:
        par[x]=y
        

def solve(A,B):
    n=A
    m=len(B)
    B.sort(key=lambda x:x[2])

    par=[i for i in range(n+1)]
    rank=[0 for i in range(n+1)]

    #print(B)
    ans=0
    for i in range(m):
        x,y=find(B[i][0],par),find(B[i][1],par)
        #print(i,x,y)
        if (x!=y):
            ans=ans+B[i][2]
            union(x,y,rank,par)
        #print(par)
    print(ans)

A = 4
B = [   [1, 2, 1],
            [2, 3, 2],
            [3, 4, 4],
            [1, 4, 3]   ]

solve(A,B)
            
        
