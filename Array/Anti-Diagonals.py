def solve(A):
    n=len(A)

    G={}
    for i in range((2*n)-1):
        G[i]=[]

    for i in range(n):
        for j in range(n):
            G[i+j].append(A[i][j])

    ans=[]
    for i in range((2*n)-1):
        ans.append(G[i])        

    return ans

print(solve([[1,2],[3,4]]))
