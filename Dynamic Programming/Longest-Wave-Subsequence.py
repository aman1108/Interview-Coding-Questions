def solve(A):
    n=len(A)
    pf=[0 for i in range(n)]
    pf[0]=0

    for i in range(1,n):
        for j in range(i):
            if (A[i]>A[j]):
                pf[i]=max(pf[i],pf[j]+1)

    sf=[0 for i in range(n)]
    sf[-1]=0
    for i in range(n-2,-1,-1):
        for j in range(n-1,i,-1):
            if (A[i]>A[j]):
                sf[i]=max(sf[i],sf[j]+1)

    ans=1
    for i in range(n):
        ans=max(ans,pf[i]+sf[i]+1)
        
    print(ans)

solve([1,2,1])
    
