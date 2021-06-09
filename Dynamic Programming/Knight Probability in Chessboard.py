def solve(n,k,st,end):
    G=[[2,1],[1,2],[-2,1],[-2,-1],[2,-1],[-1,-2],[-1,2],[1,-2]]

    Q=set()
    Q.add((st,end))
    ans=1

    DP=[[0 for i in range(n)] for j in range(n)]
    DP[st][end]=1
    for i in range(k):
        DP1=[[0 for i in range(n)] for j in range(n)]
        temp=set()
        for a,b in Q:
            for x,y in G:
                if (a+x>=0 and a+x<n and b+y>=0 and b+y<n):
                    DP1[a+x][b+y]+=DP[a][b]
                    temp.add((a+x,b+y))

        Q=temp
        DP=DP1.copy()

    s=0
    for a in DP:
        s=s+sum(a)
    return s/pow(8,k)
    
print(solve(3,0,0,0))
                    
