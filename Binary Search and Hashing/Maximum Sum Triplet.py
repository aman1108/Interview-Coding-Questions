import bisect
def solve(A):
    n=len(A)
    mv=[0 for i in range(n)]
    mv[-1]=-1

    for i in range(n-2,-1,-1):
        mv[i]=max(mv[i+1],A[i+1])

    l=[A[0]]
    lmv=[-1 for i in range(n)]
    lmv[0]=-1

    for i in range(1,n):
        a=bisect.bisect_left(l,A[i])
        a=a-1
        if (a>=0 and l[a]<A[i]):
            lmv[i]=l[a]
        bisect.insort(l,A[i])

    #print(lmv)
    ans=-1
    for i in range(n):
        if(mv[i]>A[i] and lmv[i]!=-1):
            ans=max(ans,mv[i]+lmv[i]+A[i])

    return ans

print(solve([1,2,3]))

    
print(solve([2, 5, 3, 1, 4, 9]))
