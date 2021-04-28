import bisect
def solve(A,B):
    mv=max(A)
    mod=(10**9)+7
    sieve=[1 for i in range(mv+1)]
    for i in range(2,mv+1):
        for j in range(i,mv+1,i):
            sieve[j]=(sieve[j]*i)%mod
    
    n=len(A)
    m=len(B)

    lcnt=[0 for i in range(n)]
    stk=[]
    for i in range(n):
        while(len(stk)>0 and A[stk[-1]]<=A[i]):
            stk.pop()
        if (len(stk)==0):
            lcnt[i]=i+1
        else:
            lcnt[i]=i-stk[-1]
        stk.append(i)

    rcnt=[0 for i in range(n)]
    val=[[sieve[A[i]],0] for i in range(n)]
    
    stk=[]
    for i in range(n-1,-1,-1):
        while(len(stk)>0 and A[stk[-1]]<A[i]):
            stk.pop()
        if (len(stk)==0):
            rcnt[i]=n-i
        else:
            rcnt[i]=stk[-1]-i
        stk.append(i)
        val[i][1]=rcnt[i]*lcnt[i]

    val.sort(reverse=True)
    vsum=[0 for i in range(n)]
    vsum[0]=val[0][1]
    for i in range(1,n):
        vsum[i]=vsum[i-1]+val[i][1]

    #print(val,vsum)
    ans=[]
    for i in range(m):
        v=B[i]
        ind=bisect.bisect_left(vsum,v)
        ans.append(val[ind][0])

    return ans
    
    

    

print(solve([1,1,1,1],[10]))
#print(solve([1,3],[1]))
    
