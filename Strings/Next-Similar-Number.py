def solve(A):
    n=len(A)
    G={}
    for i in range(11):
        G[i]=0

    G[int(A[-1])]=1
    s=-1
    for i in range(n-2,-1,-1):
        v=A[i]
        G[int(v)]+=1
        for j in range(int(v)+1,11):
            if (G[j]>0):
                s=A[:i]+str(j)
                G[j]-=1
                for k in range(11):
                    while (G[k]>0):
                        s=s+str(k)
                        G[k]-=1
                return s
        

    return -1
                
print(solve("4321"))
