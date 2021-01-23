def solve(A):
    n=len(A)
    A.sort()
    size=pow(2,n)
    G={}
    ans=[]
    for i in range(size):
        B=[]
        for j in range(n):
            if (i & (1<<j)>0):
                B.append(A[j])
                
        if tuple(B) not in G:
            G[tuple(B)]=1
            ans.append(B)
            
    ans.sort()         
    return ans

print(solve([1,2,3]))
